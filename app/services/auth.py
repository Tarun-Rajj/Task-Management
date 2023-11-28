from app.models import User
from app.config.db_config import SessionLocal
# from werkzeug.security import check_password_hash
from bcrypt import hashpw, gensalt, checkpw


def signup(username,password,role):
    session = SessionLocal()

    try:
        if not username or not password or not role:
            return {'error': 'Username, password, and role are required and cannot be empty'}, 400
        existing_user = session.query(User).filter(User.username == username).first()
        if existing_user:
            return {'error': 'Username is already taken'}, 400
        allowed_roles = ['admin', 'manager', 'employee']
        if role.lower() not in allowed_roles:
            return {'error': f'Invalid role. Allowed roles are: {", ".join(allowed_roles)}'}, 400
        hashed_password = hashpw(password.encode('utf-8'), gensalt())
        new_user = User(username=username, password=hashed_password, role=role.lower())
        session.add(new_user)
        session.commit()
        return {'message': 'User registered successfully'}, 201
    except Exception as e:
        session.rollback()
        return {'error': f'Error registering user: {e}'}, 500
    finally:
        session.close()


def login(username, password):
    session = SessionLocal()
    try:
        user= session.query(User).filter(User.username == username).first()
        if user and checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return{'message':'Login successful','user_id' : user.id, 'username': user.username, 'role' : user.role}
        else:
            return {'error': 'Invalid username or password'}, 401
    except Exception as e:
        return {'error': f'Error logging in: {e}'}
    finally:
        session.close()


def reset_password(username, current_password, new_password):
    session = SessionLocal()
    
    try:
        user = session.query(User).filter(User.username == username).first()

        if user:
            if checkpw(current_password.encode('utf-8'), user.password.encode('utf-8')):
                hashed_new_password = hashpw(new_password.encode('utf-8'), gensalt())
                user.password = hashed_new_password
                session.commit()

                return {'message': 'Password reset successfully'}, 200
            else:
                return {'error': 'Invalid current password'}, 401
        else:
            return {'error': 'User not found'}, 404
    except Exception as e:
        session.rollback()
        return {'error': f'Error resetting password: {e}'}, 500
    finally:
        session.close()
   


