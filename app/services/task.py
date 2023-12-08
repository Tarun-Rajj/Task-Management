from app.models import Task
from app.config.db_config import SessionLocal

def add(title, description, assigned_by_id, assigned_to_id):
    session = SessionLocal()
    try:
        new_task = Task(title=title, description=description, assigned_by_id=assigned_by_id, assigned_to_id=assigned_to_id)
        session.add(new_task)
        session.commit()
        return {'message': 'Task added successfully'}, 201
    except Exception as e:
        session.rollback()
        return {'error': f'Error adding task: {e}'}
    finally:
        session.close()

def view(task_id):
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id).first()
        if task:
            return {
                'id': task.id,
                'title': task.title,
                'description': task.description
            }
        else:
            return {'error': 'Task not found'}, 404
    except Exception as e:
        return {'error': f'Error retrieving task: {e}'}
    finally:
        session.close()
    

def viewall():
    session = SessionLocal()
    try:
        tasks = session.query(Task).all()
        task_list = [
            {
                'id': task.id,
                'title': task.title,
                'description': task.description
            }
            for task in tasks
        ]
        return task_list
    except Exception as e:
        return {'error': f'Error retrieving tasks: {e}'}
    finally:
        session.close()

def delete(id):
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == id).first()

        if task:
            session.delete(task)
            session.commit()
            return {'message': 'Task deleted successfully'}, 200
        else:
            return {'error': 'Task not found'}, 404
    except Exception as e:
        session.rollback()
        return {'error': f'Error deleting task: {e}'}
    finally:
        session.close()


def update(id, data):
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == id).first()

        if task:
                # Update task fields based on the provided data
                task.title = data.get('title', task.title)
                task.description = data.get('description', task.description)
                session.commit()
                return {'message': 'Task updated successfully'}, 200
        else:
            return {'error': 'Task not found'}, 404
    except Exception as e:
        session.rollback()
        return {'error': f'Error updating task: {e}'}
    finally:
        session.close()
    