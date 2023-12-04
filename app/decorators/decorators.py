
# app/decorators.py
from functools import wraps
from flask import request, jsonify
from app.services.auth import get_user_role
from app.services.utils import *

def requires_role(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                authorization_header = request.headers.get('Authorization')
                if not authorization_header:
                    return jsonify({'error': 'Authorization header missing'}), 401

                token = authorization_header.split()[1]
                user_id = decode_token_and_get_user_id(token)
                user_role = get_user_role(user_id)
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
                user_id = decode_token_and_get_user_id(token)

                user_role = get_user_role(user_id)
                print(f"user role is:",user_role)

                if str(user_role) in ['admin', 'manager']:

                    return func(*args, **kwargs)
                else:
                    return jsonify({'error': 'Permission denied. Admin or Manager role required.'}), 403
            except Exception as e:
                return jsonify({'error': f'Error in role check: {e}'}), 500
        

        return wrapper
    return decorator






