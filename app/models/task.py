from app.config.db_config import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum

from sqlalchemy.orm import relationship

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='tasks')
