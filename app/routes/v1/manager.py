from flask import Blueprint, request, jsonify
from app.services.admin import *
from app.decorators.permissions import requires_role_manager


manager_bp = Blueprint('manager', __name__)


@manager_bp.route('/add-employee-manager', methods=['POST'])
@requires_role_manager()
def add_employee_as():
    data = request.get_json()
    if 'username' not in data or 'password' not in data:
        return {'error': 'Username and password are required'}, 400
  
    result = add_employee(data)
    return jsonify(result)
