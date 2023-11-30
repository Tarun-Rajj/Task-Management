from .task import *
# from flask import Flask, Jsonify
# from app.routes.task import *

class Role(enum.Enum):
    admin = 'admin'
    manager = 'manager'
    employee = 'employee'

    def __str__(self):
        return self.value

