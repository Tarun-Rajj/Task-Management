from app.models import User,Role
from app.config.db_config import SessionLocal
from bcrypt import hashpw, gensalt, checkpw
from .utils import *



def registered(username, password, email, role):
    session = SessionLocal()
    try:
        existing_user = session.query(User).filter(User.username == username).first()
        if existing_user:
            return {'error': 'Username is already taken'}, 400
        allowed_roles = ['admin', 'manager', 'employee']
        if role not in allowed_roles:
            return {'error': f'Invalid role. Allowed roles are: {", ".join(allowed_roles)}'}, 400
        hashed_password = hash_password(password)
        new_user = User(username=username, password=hashed_password, email=email, role=Role[role.lower()])
        session.add(new_user)
        session.commit()
        return {'message': 'User registered successfully'}, 201
    except Exception as e:
        session.rollback()
        return {'error': f'Error registering user: {e}'}, 500
    finally:
        session.close()
            
def signin(username, password):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.username == username).first()
        if user and validate_password(password, user.password):
            return {
                'message': 'Login successful',
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.role
            }
        else:
            return {'error': 'Invalid username or password'}, 401
    except Exception as e:
        return {'error': f'Error logging in: {e}'}
    finally:
        session.close()

def change(username, current_password, new_password):
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


def forgot(username):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.username == username).first()
        if user:
            reset_token = generate_reset_token()
            user.reset_token = reset_token
            session.commit()
            send_password_reset_email(user.email, reset_token)
            return {'message': 'Password reset email sent successfully. Check your email for instructions.'}, 200
        else:
            return {'error': 'User not found'}, 404
    except Exception as e:
        session.rollback()
        return {'error': f'Error initiating forgot password process: {e}'}, 500
    finally:
        session.close()
   



