from config.db_config import Base
from sqlalchemy import Column, Integer, String


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
   