from flask import Blueprint, request, jsonify
from app.services import *
# from app.config import MAIL_SERVER

auth_bp=Blueprint('auth',__name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json() 
    username = data['username']
    password = data['password']
    email = data['email']
    role = data.get('role', 'employee')
    if not username or not password or not email or not role:
        return {'error': 'Username, password, email and role are required and cannot be empty'}, 400
    result = registered(username, password, email, role)
    return jsonify(result),201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username=data['username']
    password=data['password']
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return {'error': 'Username and password and email are required'}, 400
    result= signin(username, password)
    return jsonify(result),201


@auth_bp.route('/reset', methods=['POST'])
def reset():
    data = request.get_json()
    if 'username' not in data or 'current_password' not in data or 'new_password' not in data:
        return {'error': 'Username, current password, and new password are required'}, 400
    username = data['username']
    current_password = data['current_password']
    new_password = data['new_password']
    result = change(username, current_password, new_password)
    return jsonify(result),201 

@auth_bp.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.get_json()
    if 'username' not in data:
        return {'error': 'Username is required'}, 400  
    username = data['username']
    result = forgot(username)
    return jsonify(result),201