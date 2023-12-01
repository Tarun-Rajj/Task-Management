from flask import Flask 
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from app.config import *

load_dotenv()
import os
db = SQLAlchemy()
mail=Mail()

def create_app():
    app = Flask(__name__)
    from app.routes.task import task_bp
    from app.routes.auth import auth_bp
    from app.routes.admin import admin_bp
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    app.config.from_object('app.config.config')
    db.init_app(app)
    mail.init_app(app)
    app.register_blueprint(task_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    return app 

create_app()

