
# app/decorators.py
from functools import wraps
from flask import request, jsonify
from app.services.auth import get_user_role
from app.services.utils import *
import jwt

def requires_role(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                authorization_header = request.headers.get('Authorization')
                if not authorization_header:
                    return jsonify({'error': 'Authorization header missing'}), 401

                token = authorization_header.split()[1]
                id = decode_token_and_get_user_id(token)
                user_role = get_user_role(id)
                print(user_role)
                print(required_role)
                if str(user_role) == required_role:
                    return func(*args, **kwargs)
                else: 
                    return jsonify({'error': 'Permission denied admin role required.'}), 403
            except Exception as e:
                return jsonify({'error': f'Error in role check: {e}'}), 500
        return wrapper
    return decorator


def requires_role_manager():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                authorization_header = request.headers.get('Authorization')
                if not authorization_header:
                    return jsonify({'error': 'Authorization header missing'}), 401
                token = authorization_header.split()[1]
                id = decode_token_and_get_user_id(token)
                print(id)

                user_role = get_user_role(id)
                print(f"user role is:",user_role)

                if str(user_role) in ['admin', 'manager']:

                    return func(*args, **kwargs)
                else:
                    return jsonify({'error': 'Permission denied. Admin or Manager role required.'}), 403
            except Exception as e:
                return jsonify({'error': f'Error in role check: {e}'}), 500
        return wrapper
    return decorator

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization', '')

        if not auth_header or not auth_header.lower().startswith('bearer '):
            return jsonify({'message': 'Authorization header must start with Bearer'}), 401

        parts = auth_header.split()

        if len(parts) == 1:
            return jsonify({'message': 'Token not found'}), 401
        elif len(parts) > 2:
            return jsonify({'message': 'Authorization header must be Bearer + \s + token'}), 401

        token = parts[1]

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user_id = data['id']
            current_user_role = data['role']
            print("currentuser",current_user_id, current_user_role)

        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError as e:
            print(f"Invalid Token: {e}")
            return jsonify({'message': 'Invalid token!'}), 401
        return f(current_user_id, current_user_role, *args, **kwargs)

    return decorated_function











