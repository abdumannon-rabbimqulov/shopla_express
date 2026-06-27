from sqlalchemy.ext.asyncio import AsyncSession
from repositories.courier_repo import CourierRepository

class AdminService:
    def __init__(self, db: AsyncSession):
        self.repo = CourierRepository(db)

    async def get_pending_couriers(self):
        return await self.repo.get_pending_couriers()

    async def approve_courier(self, courier_id: str):
        courier = await self.repo.get_by_id(courier_id)
        if not courier:
            raise ValueError("Courier not found")
            
        if courier.status == "ACTIVE":
            return courier
            
        return await self.repo.update_status(courier, "ACTIVE")
