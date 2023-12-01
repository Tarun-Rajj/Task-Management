# app/services/admin.py
from app.models import User, SessionLocal

def add_manager(username, password):
    session = SessionLocal()
    try:
        existing_user = session.query(User).filter(User.username == username).first()
        if existing_user:
            return {'error': 'Username is already taken'}, 400
        new_user = User(username=username, password=password, role='manager')
        session.add(new_user)
        session.commit()
        return {'message': 'Manager added successfully'}, 201
    except Exception as e:
        session.rollback()
        return {'error': f'Error adding manager: {e}'}, 500
    finally:
        session.close()



def add_employee(username, password):
    session = SessionLocal()
    try:
        existing_user = session.query(User).filter(User.username == username).first()
        if existing_user:
            return {'error': 'Username is already taken'}, 400
        new_user = User(username=username, password=password, role='employee')
        session.add(new_user)
        session.commit()
        return {'message': 'Employee added successfully'}, 201
    except Exception as e:
        session.rollback()
        return {'error': f'Error adding employee: {e}'}, 500
    finally:
        session.close()

