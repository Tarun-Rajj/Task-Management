from typing import Optional
from sqlalchemy.orm import Session
from app.models import Task
from app.config.db_config import SessionLocal

def add_task(session: Optional[Session] = None, title: str = None, description: str = None) -> dict:
    if session is None:
        session = SessionLocal()

    if title is None or description is None:
        return {'error': 'Title and description are required'}, 400

    try:
        new_task = Task(title=title, description=description)
        print("SZDFDFG")
        session.add(new_task)
        print("dsfdgg")
        session.commit()
        print("aaaaaaaaaaa")
        return {'message': 'Task added successfully'}, 201
    except Exception as e:
        session.rollback()
        return {'error': f'Error adding task: {e}'}, 500
    finally:
        session.close()
