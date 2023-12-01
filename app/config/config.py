# app/config/config.py
import os

DEBUG = True
SECRET_KEY = os.getenv('SECRET_KEY')
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587  # This might vary based on your email provider
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'tarunkumar86437@gmail.com'
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER = 'tarunkumar86437@gmail.com'
