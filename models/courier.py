from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.sql import func
import uuid
from db.database import Base

class Courier(Base):
    __tablename__ = "couriers"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=True) # Will be filled in step 3
    password_hash = Column(String, nullable=False)
    
    # Vehicle and Docs
    vehicle_type = Column(String, nullable=False, default="SCOOTER") # SCOOTER, CAR
    passport_front_url = Column(String, nullable=True)
    passport_back_url = Column(String, nullable=True)
    texpassport_front_url = Column(String, nullable=True)
    texpassport_back_url = Column(String, nullable=True)
    
    # AI Extracted Fields (populated later)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    pinfl = Column(String, nullable=True)
    passport_number = Column(String, nullable=True)
    car_plate_number = Column(String, nullable=True)
    car_model = Column(String, nullable=True)

    status = Column(String, default="PENDING") # PENDING, ACTIVE, REJECTED
    created_at = Column(DateTime(timezone=True), server_default=func.now())
