from flask import Flask 
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


load_dotenv()
import os
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    from app.routes.add_task import add_task_bp
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
    db.init_app(app)
    app.register_blueprint(add_task_bp)
    return app 

create_app()

