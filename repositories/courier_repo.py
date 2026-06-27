from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.courier import Courier
from typing import List, Optional

class CourierRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, courier_id: str) -> Optional[Courier]:
        result = await self.db.execute(select(Courier).where(Courier.id == courier_id))
        return result.scalars().first()

    async def get_by_phone(self, phone: str) -> Optional[Courier]:
        result = await self.db.execute(select(Courier).where(Courier.phone == phone))
        return result.scalars().first()

    async def get_pending_couriers(self) -> List[Courier]:
        result = await self.db.execute(select(Courier).where(Courier.status == "PENDING"))
        return result.scalars().all()

    async def create_courier(self, phone: str, password_hash: str, front_url: str, back_url: str) -> Courier:
        new_courier = Courier(
            phone=phone,
            password_hash=password_hash,
            passport_front_url=front_url,
            passport_back_url=back_url,
            status="PENDING"
        )
        self.db.add(new_courier)
        await self.db.commit()
        await self.db.refresh(new_courier)
        return new_courier

    async def update_status(self, courier: Courier, status: str) -> Courier:
        courier.status = status
        await self.db.commit()
        await self.db.refresh(courier)
        return courier
