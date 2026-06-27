from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from db.database import get_db
from schemas.courier import CourierResponse
from services.admin_service import AdminService

router = APIRouter(prefix="/api/v1/admin", tags=["Admin"])

@router.get("/couriers/pending", response_model=List[CourierResponse])
async def get_pending_couriers(db: AsyncSession = Depends(get_db)):
    service = AdminService(db)
    return await service.get_pending_couriers()

@router.post("/couriers/{courier_id}/approve")
async def approve_courier(courier_id: str, db: AsyncSession = Depends(get_db)):
    service = AdminService(db)
    try:
        courier = await service.approve_courier(courier_id)
        return {"message": f"Courier {courier.phone} approved and is now ACTIVE."}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
