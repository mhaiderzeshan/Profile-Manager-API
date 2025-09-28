from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from enum import Enum


class UserRole(str, Enum):
    student = "student"
    mentor = "mentor"


class ProfileBase(BaseModel):
    name: str = Field(..., max_length=50)
    email: EmailStr
    role: UserRole


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=20)
    email: Optional[EmailStr] = None
    role: Optional[str] = Field(None, max_length=20)


class Profile(ProfileBase):
    id: int

    class Config:
        from_attributes = True
