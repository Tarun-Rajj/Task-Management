from .role import *
from .task import *
from sqlalchemy.orm import relationship
# from services.utils import *
import bcrypt

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50),nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(254), unique=True, nullable=False)
    role = Column(Enum(Role), nullable=False)
    tasks = relationship('Task', back_populates='user')
#one to many relationship
    tasks_assigned_by = relationship('Task', foreign_keys=[Task.assigned_by_id], back_populates='assigned_by')
    tasks_assigned_to = relationship('Task', foreign_keys=[Task.assigned_to_id], back_populates='assigned_to')
    
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)