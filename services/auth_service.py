import json
import redis.asyncio as redis
import os
import shutil
import uuid
from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from repositories.courier_repo import CourierRepository
from core.security import get_password_hash
from core.config import settings

class AuthService:
    def __init__(self, db: AsyncSession):
        self.repo = CourierRepository(db)
        self.redis_client = redis.from_url(settings.REDIS_URL, decode_responses=True)

    async def process_step1(self, email: str) -> str:
        import random
        import uuid
        from services.email_service import send_otp_email
        
        # Check if already registered
        existing = await self.repo.get_by_email(email)
        if existing:
            raise ValueError("Email is already registered.")
            
        otp = str(random.randint(100000, 999999))
        token = str(uuid.uuid4())
        state = {"email": email, "otp": otp, "step": 1}
        await self.redis_client.set(f"reg_state:{token}", json.dumps(state), ex=600)
        
        # Send actual email
        await send_otp_email(email, otp)
        
        return token

    async def process_step2(self, token: str, otp_code: str, password: str):
        state_str = await self.redis_client.get(f"reg_state:{token}")
        if not state_str:
            raise ValueError("Session expired or not found")
            
        state = json.loads(state_str)
        if state["otp"] != otp_code:
            raise ValueError("Invalid OTP")
            
        state["password_hash"] = get_password_hash(password)
        state["step"] = 2
        await self.redis_client.set(f"reg_state:{token}", json.dumps(state), ex=600)

    async def process_step3(
        self, 
        token: str, 
        phone: str, 
        vehicle_type: str,
        passport_front: UploadFile, 
        passport_back: UploadFile,
        texpassport_front: UploadFile | None = None,
        texpassport_back: UploadFile | None = None
    ):
        state_str = await self.redis_client.get(f"reg_state:{token}")
        if not state_str:
            raise ValueError("Session expired or not found")
            
        state = json.loads(state_str)
        if state.get("step") != 2:
            raise ValueError("Please complete previous steps first")

        if vehicle_type == "CAR":
            if not texpassport_front or not texpassport_back:
                raise ValueError("Technical passport is required for cars")

        os.makedirs("uploads", exist_ok=True)
        front_path = f"uploads/{uuid.uuid4()}_front.jpg"
        back_path = f"uploads/{uuid.uuid4()}_back.jpg"
        
        with open(front_path, "wb") as buffer:
            shutil.copyfileobj(passport_front.file, buffer)
        with open(back_path, "wb") as buffer:
            shutil.copyfileobj(passport_back.file, buffer)

        tex_front_path = None
        tex_back_path = None
        if vehicle_type == "CAR" and texpassport_front and texpassport_back:
            tex_front_path = f"uploads/{uuid.uuid4()}_tex_front.jpg"
            tex_back_path = f"uploads/{uuid.uuid4()}_tex_back.jpg"
            with open(tex_front_path, "wb") as buffer:
                shutil.copyfileobj(texpassport_front.file, buffer)
            with open(tex_back_path, "wb") as buffer:
                shutil.copyfileobj(texpassport_back.file, buffer)

        # Use repo to create record
        courier = await self.repo.create_courier(
            email=state["email"],
            phone=phone,
            password_hash=state["password_hash"],
            front_url=front_path,
            back_url=back_path,
            vehicle_type=vehicle_type,
            texpassport_front_url=tex_front_path,
            texpassport_back_url=tex_back_path
        )
        
        await self.redis_client.delete(f"reg_state:{token}")
        return courier
