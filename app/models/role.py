from .task import *
import enum


class Role(enum.Enum):
    admin = 'admin'
    manager = 'manager'
    employee = 'employee'

    def __str__(self):
        return self.value

