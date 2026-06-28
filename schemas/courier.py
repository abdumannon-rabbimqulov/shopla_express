from pydantic import BaseModel, Field

class RegisterStep1(BaseModel):
    email: str = Field(..., description="Courier email address")

class RegisterStep2(BaseModel):
    email: str
    otp_code: str
    password: str

class CourierResponse(BaseModel):
    id: str
    email: str
    phone: str | None
    status: str
    
    class Config:
        orm_mode = True
