from flask import Blueprint, request, jsonify
from app.services import add_task

add_task_bp = Blueprint('add_task', __name__)

@add_task_bp.route('/addtask', methods=['POST'])
def add_task_route():
    data=request.get_json()
    return jsonify(add_task(title=data.get('title'),description=data.get('description')))
  