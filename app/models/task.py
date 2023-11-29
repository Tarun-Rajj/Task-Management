from app.config.db_config import Base
from sqlalchemy import Column, Integer, String, Enum
import enum


class Role(enum.Enum):
    admin = 'admin'
    manager = 'manager'
    employee = 'employee'

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50),nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(254), unique=True, nullable=False)
    role = Column(Enum(Role), nullable=False)


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
