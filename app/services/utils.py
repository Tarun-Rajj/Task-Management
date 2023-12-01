import bcrypt
from app.config import mail
import uuid
from flask_mail import Message  

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