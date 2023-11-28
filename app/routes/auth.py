from flask import Blueprint, request, jsonify
from app.services import signup
from app.services import login
from app.services import reset_password

auth_bp=Blueprint('auth',__name__)

@auth_bp.route('/signup', methods=['POST'])
def signup_route():
    data = request.get_json()
    
    username = data['username']
    password = data['password']
    role = data.get('role', 'employee')

    result = signup(username, password, role)
    return jsonify(result)

@auth_bp.route('/login', methods=['POST'])
def login_route():
    data = request.get_json()

    if 'username' not in data or 'password' not in data:
        return {'error': 'Username and password are required'}, 400

    username=data['username']
    password=data['password']

    result= login(username, password)
    return jsonify(result)


@auth_bp.route('/reset-password', methods=['POST'])
def reset_password_route():
    data = request.get_json()
    if 'username' not in data or 'current_password' not in data or 'new_password' not in data:
        return {'error': 'Username, current password, and new password are required'}, 400

    username = data['username']
    current_password = data['current_password']
    new_password = data['new_password']
    result = reset_password(username, current_password, new_password)

    return jsonify(result) 

