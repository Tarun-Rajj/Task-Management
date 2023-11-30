# app/decorators.py
from functools import wraps
from flask import request, jsonify
from app.services.auth import get_user_role
from app.services.utils import *
def requires_role(required_role):
    def decorator(func):                                                       #It takes function as an arguments 
        @wraps(func)                                                             # It is used to decorate the wrapper function
        def wrapper(*args, **kwargs):                                                   #This preserves the original fxn name and docstring
            try:                  #allow the wrapper to accept any number of positional and keyword arguments.
                # Get the JWT from the Authorization header
                authorization_header = request.headers.get('Authorization')
                if not authorization_header:
                    return jsonify({'error': 'Authorization header missing'}), 401

                # Extract the token from the header (assuming 'Bearer' scheme)
                token = authorization_header.split()[1]
                print(token)

                user_id = decode_token_and_get_user_id(token)

                print(f"print user_id:",user_id) 
                # Call get_user_role with the decoded token
                user_role = get_user_role(user_id)
                print(f"print role",user_role)
                print(str(user_role) == required_role)
                print(required_role)
    
                if str(user_role) == required_role:
                    return func(*args, **kwargs)
                else:
                    return jsonify({'error': 'Permission denied. Admin role required.'}), 403
            except Exception as e:
                return jsonify({'error': f'Error in admin role check: {e}'}), 500
        return wrapper
    return decorator


