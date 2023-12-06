from .role import *
from .task import *
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50),nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(254), unique=True, nullable=False)
    role = Column(Enum(Role), nullable=False)

    tasks_assigned_by = relationship('Task', foreign_keys='Task.assigned_by_id', backref='assigned_by')
    tasks_assigned_to = relationship('Task', foreign_keys='Task.assigned_to_id', backref='assigned_to')
