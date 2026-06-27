from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.sql import func
import uuid
from db.database import Base

class Courier(Base):
    __tablename__ = "couriers"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    phone = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    passport_front_url = Column(String, nullable=True)
    passport_back_url = Column(String, nullable=True)
    status = Column(String, default="PENDING") # PENDING, ACTIVE, REJECTED
    created_at = Column(DateTime(timezone=True), server_default=func.now())
