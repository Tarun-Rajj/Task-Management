from flask import Flask 
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


load_dotenv()
import os
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    from app.routes.task import task_bp
    from app.routes.auth import auth_bp
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
    db.init_app(app)
    app.register_blueprint(task_bp)
    app.register_blueprint(auth_bp)
    return app 

create_app()

