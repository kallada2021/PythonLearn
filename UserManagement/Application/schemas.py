from pydantic import BaseModel
from typing import List
from database import SessionLocal

class UserBase(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    gender: str
    country: str
    is_active: bool

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()