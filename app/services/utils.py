import bcrypt
from app import mail
import uuid
from flask_mail import Message 
import os
import jwt
from datetime import datetime, timedelta
from flask import current_app 

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def validate_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

   
def generate_reset_token():
    return str(uuid.uuid4())


def send_password_reset_email(email, reset_token):
    try:
        # Create a Flask-Mail message
        subject = 'Password Reset Request'
        body = f'Click the following link to reset your password: /reset-password/{reset_token}'
        message = Message(subject=subject, recipients=[email], body=body)
        # Send the email
        mail.send(message)
        return {'message': 'Password reset email sent successfully. Check your email for instructions.'}, 200
    except Exception as e:
        return {'error': f'Error sending password reset email: {e}'}, 500
    
import jwt
from flask import current_app
def decode_token_and_get_user_id(token):
    try:
        secret_key = current_app.config.get('SECRET_KEY')  # Make sure your app has a secret key
        decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
        id = decoded_token.get('id')  # Assuming 'id' contains the user ID
        return id
    except jwt.ExpiredSignatureError:
        raise Exception('Token has expired')
    except jwt.InvalidTokenError:
        raise Exception('Invalid token')
    except Exception as e:
        raise Exception(f'Error decoding token: {e}')
    

def generate_jwt_token(id, username, role):
    SECRET_KEY = os.getenv('SECRET_KEY')
    if SECRET_KEY is None:
        raise ValueError('SECRET_KEY not set in the environment variables')
    expiration_time = datetime.utcnow() + timedelta(days=1)
    payload = {
        'id': id,
        'username': username,
        'role': role,
        'exp': expiration_time
    }
    token = jwt.encode(payload, os.getenv('SECRET_KEY') , algorithm='HS256')
    return token

