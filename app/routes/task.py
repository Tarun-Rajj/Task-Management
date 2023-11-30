from flask import Blueprint, request, jsonify
from app.services import *

task_bp = Blueprint('add_task', __name__)


@task_bp.route('/', methods=['POST'])
def add_task():
    data=request.get_json()
    if not data.get('title') or not data.get('description'):
        return jsonify({'error': 'Title and description cannot be empty'}), 400
    result = add(title=data.get('title'), description=data.get('description'))
    return jsonify(result),201


@task_bp.route('/<task_id>', methods=['GET'])
def view_task(task_id):
    if task_id is None:
        return jsonify({'error': 'Task ID is required'}), 400
    task = view(task_id)
    if task:
        return jsonify(task)
    else:
        return jsonify({'error': 'Task not found'}), 404
    
    
@task_bp.route('/', methods=['GET'])
def view_all_tasks():
    tasks = viewall()
    return jsonify(tasks),201

@task_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id=None):
    if task_id is None:
        return jsonify({'error': 'Task ID is required'}), 400
    result = delete(task_id)
    return jsonify(result),201


@task_bp.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    if task_id is None:
        return jsonify({'error': 'Task ID is required'}), 400
    if not data:
        return jsonify({'error': 'No data provided for update'}), 400
    result = update(task_id, data)
    return jsonify(result),201


# @task_bp.route('/')
# def home():
#     role = Role.admin.value
#     print(jsonify(role=role))
#     return jsonify(role=role)