# app/schemas/user.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from uuid import UUID

# 🚨 NAME CHECKING: Exact spelling match huna parcha sathi!
class UserCreatePlain(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)

class UserResponse(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    auth_provider: str

    class Config:
        from_attributes = True


class UserLoginSchema(BaseModel):
    email:EmailStr
    password:str 