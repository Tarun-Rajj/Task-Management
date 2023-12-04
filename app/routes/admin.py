from flask import Blueprint, request, jsonify
from app.services.admin import *
from app.decorators import requires_role
admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/add-manager', methods=['POST'])
@requires_role('admin')
def add_manager_route():
    data = request.get_json()
    if 'username' not in data or 'password' not in data:
        return {'error': 'Username and password are required'}, 400
    result = add_manager(data)
    return jsonify(result)

@admin_bp.route('/add-employee', methods=['POST'])
@requires_role('admin')
def add_employee_route():
    data = request.get_json()
    if 'username' not in data or 'password' not in data:
        return {'error': 'Username and password are required'}, 400
    
    result = add_employee(data)
    return jsonify(result)
