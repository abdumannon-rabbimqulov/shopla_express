from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from schemas.courier import RegisterStep1, RegisterStep2
from services.auth_service import AuthService

router = APIRouter(prefix="/api/v1/auth", tags=["Auth"])

@router.post("/register-step1")
async def register_step1(data: RegisterStep1, db: AsyncSession = Depends(get_db)):
    service = AuthService(db)
    try:
        mock_otp = await service.process_step1(data.phone)
        return {"message": "OTP sent successfully", "mock_otp": mock_otp}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/register-step2")
async def register_step2(data: RegisterStep2, db: AsyncSession = Depends(get_db)):
    service = AuthService(db)
    try:
        await service.process_step2(data.phone, data.otp_code, data.password)
        return {"message": "OTP verified and password set. Please upload passports to complete registration."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/register-step3")
async def register_step3(
    phone: str = Form(...),
    vehicle_type: str = Form(..., description="SCOOTER or CAR"),
    passport_front: UploadFile = File(...),
    passport_back: UploadFile = File(...),
    texpassport_front: UploadFile | None = File(None),
    texpassport_back: UploadFile | None = File(None),
    db: AsyncSession = Depends(get_db)
):
    service = AuthService(db)
    try:
        courier = await service.process_step3(
            phone=phone, 
            vehicle_type=vehicle_type,
            passport_front=passport_front, 
            passport_back=passport_back,
            texpassport_front=texpassport_front,
            texpassport_back=texpassport_back
        )
        return {"message": "Registration complete! Your account is pending admin approval.", "courier_id": courier.id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
