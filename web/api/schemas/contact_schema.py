from pydantic import BaseModel, EmailStr
from datetime import datetime

class ContactCreate(BaseModel):
    Name: str
    Email: EmailStr
    Message: str

class ContactRead(ContactCreate):
    Id: int
    SentAt: datetime

    class Config:
        orm_mode = True