from flask import Flask 
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
db = SQLAlchemy()
load_dotenv()
import os

mail=Mail()

def create_app():
    app = Flask(__name__)
    from app.routes.v1.task import task_bp
    from app.routes.v1.auth import auth_bp
    from app.routes.v1.admin import admin_bp
    from app.routes.v1.manager import manager_bp
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY") 
    db.init_app(app)
    mail.init_app(app)
    app.register_blueprint(task_bp,url_prefix='/api/v1')
    app.register_blueprint(auth_bp,url_prefix='/api/v1')
    app.register_blueprint(admin_bp, url_prefix='/api/v1')
    app.register_blueprint(manager_bp, url_prefix='/api/v1')
    return app 
create_app()

