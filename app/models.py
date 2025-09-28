from sqlalchemy import Column, String, Enum, Integer
import enum
from app.database import Base


class UserRole(str, enum.Enum):
    student = "student"
    mentor = "mentor"


class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    role = Column(Enum(UserRole))
