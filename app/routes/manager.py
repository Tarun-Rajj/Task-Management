from flask import Blueprint, request, jsonify
from app.services.manager import *
from app.decorators import requires_role_manager
from app.decorators import requires_role

manager_bp = Blueprint('manager', __name__)


@manager_bp.route('/add-employee-manager', methods=['POST'])
@requires_role_manager()
@requires_role('manager')
def add_employee_as():
    data = request.get_json()
    if 'username' not in data or 'password' not in data:
        return {'error': 'Username and password are required'}, 400
  
    result = add_employee_as_manager(data)
    return jsonify(result)
