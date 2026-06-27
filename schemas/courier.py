from pydantic import BaseModel, Field

class RegisterStep1(BaseModel):
    phone: str = Field(..., description="Courier phone number, e.g. +998901234567")

class RegisterStep2(BaseModel):
    phone: str
    otp_code: str
    password: str

class CourierResponse(BaseModel):
    id: str
    phone: str
    status: str
    
    class Config:
        orm_mode = True
