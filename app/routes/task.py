from flask import Blueprint, request, jsonify
from app.services import *
from app.decorators import *

task_bp = Blueprint('add_task', __name__)


@task_bp.route('/', methods=['POST'])

@token_required
@requires_role_manager()
def add_task(current_user):
    data=request.get_json()
    if not data.get('title') or not data.get('description'):
        return jsonify({'error': 'Title and description cannot be empty'}), 400
    result=add(data)
    return jsonify(result),201


@task_bp.route('/<task_id>', methods=['GET'])
@token_required
def view_task(current_user, task_id):
    if task_id is None:
        return jsonify({'error': 'Task ID is required'}), 400
    if current_user.role == Role.admin or current_user.role == Role.manager:
        task = view(task_id)
        if task:
            return jsonify(task)
        else:
            return jsonify({'error': 'Task not found'}), 404
        
    
@task_bp.route('/', methods=['GET'])
@token_required
def view_all_tasks(current_user):
    tasks = viewall()
    return jsonify(tasks),201

@task_bp.route('/<int:task_id>', methods=['DELETE'])
@token_required
def delete_task(current_user,task_id=None):
    if task_id is None:
        return jsonify({'error': 'Task ID is required'}), 400
    result = delete(task_id)
    return jsonify(result),201


@task_bp.route('/<int:task_id>', methods=['PUT'])
@token_required
def update_task(current_user,task_id):
    data = request.get_json()
    if task_id is None:
        return jsonify({'error': 'Task ID is required'}), 400
    if not data:
        return jsonify({'error': 'No data provided for update'}), 400
    result = update(task_id, data)
    return jsonify(result),201


