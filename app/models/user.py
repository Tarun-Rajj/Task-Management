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
    tasks = relationship('Task', back_populates='user')