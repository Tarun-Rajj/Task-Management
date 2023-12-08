from flask import Blueprint, request, jsonify
from app.services import *
from app.decorators.permissions import *
from app.models import *
from app.config.db_config import *

task_bp = Blueprint('add_task', __name__)


@task_bp.route('/', methods=['POST'])

@token_required
@requires_role_manager()
def add_task(current_user_id,result):
    data=request.get_json()
    if not data.get('title') or not data.get('description'):
        return jsonify({'error': 'Title and description cannot be empty'}), 400
    result=add(title=data.get('title'), description=data.get('description'), assigned_by_id=current_user_id, assigned_to_id=data.get('assigned_to_id'))
    return jsonify(result),201

def view_task_by_role(current_user_id, current_user_role, task_id):
    session = SessionLocal()
    try:
        if current_user_role == 'admin':
            task = session.query(Task).filter(Task.id==task_id).first()
        elif current_user_role ==  'manager':
            task = session.query(Task).filter(Task.id == task_id, Task.assigned_by_id == current_user_id).first()
        elif current_user_role == 'employee':
            task = session.query(Task).filter(Task.id == task_id, Task.assigned_to_id == current_user_id).first()
        else:
            return{'error': 'Invalid role'}, 401
        if task:
            return {
                'id': task.id,
                'title': task.title,
                'description' : task.description
            }
        else:
            return {'error':'Task not found'}, 404
    except Exception as e:
        return {'error': f'Error retrieving task: {e}'}, 500
    finally:
        session.close()

@task_bp.route('/<task_id>', methods=['GET'])
@token_required
def view_task(current_user_id, current_user_role, task_id):
    return view_task_by_role(current_user_id, current_user_role, task_id)

   
@task_bp.route('/', methods=['GET'])
@token_required
@requires_role('admin')
def view_all_tasks(tasks,a):
    tasks = viewall()
    if not tasks:
        return jsonify({'error': 'No Tasks Found'}), 404
    return jsonify(tasks),201

@task_bp.route('/<int:task_id>', methods=['DELETE'])
@token_required
def delete_task(current_user_id, current_user_role, task_id):
    if current_user_role == 'employee':
        return jsonify({'error': 'You are not authorized to delete the task'}), 403
    result = delete(task_id, current_user_id, current_user_role)
    return jsonify(result), 201


@task_bp.route('/<int:task_id>', methods=['PUT'])
@token_required
def update_task(current_user_id, current_user_role,task_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided for update'}), 400
    result = update(task_id, data, current_user_id,current_user_role)
    return jsonify(result),201






     

   