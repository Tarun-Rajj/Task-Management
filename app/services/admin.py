# app/services/admin.py
from app.models import User
from app.config.db_config import SessionLocal
from app.services.utils import *



def add_manager(data):
    session = SessionLocal()
    try:
        existing_user = session.query(User).filter(User.username == data['username']).first()
        if existing_user:
            return {'error': 'Username is already taken'}, 400
        # hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        hashed_password = hash_password(data['password'])
        new_user = User(username=data['username'], password=hashed_password, email= data['email'], role='manager')
        session.add(new_user)
        session.commit()
        return {'message': 'Manager added successfully'}, 201
    except Exception as e:
        session.rollback()
        return {'error': f'Error adding manager: {e}'}
    finally:
        session.close()



def add_employee(data):
    session = SessionLocal()
    try:
        existing_user = session.query(User).filter(User.username == data['username']).first()
        if existing_user:
            return {'error': 'Username is already taken'}, 400
        # hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        hashed_password = hash_password(data['password'])
        new_user = User(username=data['username'], password=hashed_password, email= data['email'], role='employee')
        session.add(new_user)
        session.commit()
        return {'message': 'Employee added successfully'}, 201
    except Exception as e:
        session.rollback()
        return {'error': f'Error adding employee: {e}'}
    finally:
        session.close()



