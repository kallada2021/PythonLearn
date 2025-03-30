from sqlalchemy import Boolean, Column, Integer, String
from database import Base, engine

# Task 2 - Code Here
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    country = Column(String)
    is_active = Column(Boolean)
    hashed_password = Column(String)
    username = Column(String, unique=True)
# ------------------------------
Base.metadata.create_all(engine)