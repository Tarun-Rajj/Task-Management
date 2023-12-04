from app.config.db_config import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
import enum
from sqlalchemy.orm import relationship


class TaskStatus(enum.Enum):
    PENDING = 'PENDING'
    IN_PROGRESS = 'IN PROGRESS'
    SENT_FOR_APPROVAL = 'SENT FOR APPROVAL'
    APPROVED = 'APPROVED'

    def __str__(self):
        return self.value



class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    status = Column(Enum(TaskStatus), nullable=False, default=TaskStatus.PENDING)

    assigned_by_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    assigned_by = relationship('User', foreign_keys=[assigned_by_id], back_populates='tasks_assigned_by')

    assigned_to_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    assigned_to = relationship('User', foreign_keys=[assigned_to_id], back_populates='tasks_assigned_to')

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='tasks')
#many to one relationship