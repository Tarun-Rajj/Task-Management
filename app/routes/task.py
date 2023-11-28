from flask import Blueprint, request, jsonify
from app.services import add_task
from app.services import view_task
from app.services import view_all_tasks
from app.services import delete_task
from app.services import update_task

task_bp = Blueprint('add_task', __name__)


@task_bp.route('/addtask', methods=['POST'])
def add_task_route():
    data=request.get_json()
    if not data.get('title') or not data.get('description'):
        return jsonify({'error': 'Title and description cannot be empty'}), 400

    result = add_task(title=data.get('title'), description=data.get('description'))
    return jsonify(result)


@task_bp.route('/viewtask/<task_id>', methods=['GET'])
def view_task_route(task_id):
    if task_id is None:
        return jsonify({'error': 'Task ID is required'}), 400
    task = view_task(task_id)
    if task:
        return jsonify(task)
    else:
        return jsonify({'error': 'Task not found'}), 404
    
    
@task_bp.route('/viewalltasks', methods=['GET'])
def view_all_tasks_route():
    tasks = view_all_tasks()
    return jsonify(tasks)

@task_bp.route('/deletetask/<int:task_id>', methods=['DELETE'])
def delete_task_route(task_id=None):
    if task_id is None:
        return jsonify({'error': 'Task ID is required'}), 400
    result = delete_task(task_id)
    return jsonify(result)


@task_bp.route('/updatetask/<int:task_id>', methods=['PUT'])
def update_task_route(task_id):
    data = request.get_json()
    if task_id is None:
        return jsonify({'error': 'Task ID is required'}), 400
    if not data:
        return jsonify({'error': 'No data provided for update'}), 400
    result = update_task(task_id, data)
    return jsonify(result)


