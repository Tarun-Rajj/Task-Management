from flask import Blueprint, request, jsonify
from app.services import *
from app.decorators.permissions import *
from app.validators import *
# from app.config import MAIL_SERVER

auth_bp=Blueprint('auth',__name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data= request.get_json()
    error = validate_user_data(data)
    if error:
        return jsonify(error), 400
    result = registered(**data)
    return jsonify(result), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data= request.get_json()
    error= validate_user_login(data)
    if error:
        return jsonify(error), 400
    result= signin(**data)
    return jsonify(result), 201


@auth_bp.route('/reset', methods=['POST'])
@token_required
def reset(current_user_id, current_user_role):
    data = request.get_json()
    error= validate_user_reset(data)
    if error:
        return jsonify(error), 400
    result = change(**data)
    return jsonify(result), 201 


@auth_bp.route('/forgot-password', methods=['POST'])
@token_required
def forgot_password(current_user_id, current_user_role):
    data = request.get_json()
    error= validate_user_forgot_password(data)
    if error:
        return jsonify(error), 400
    result = send_forgot_pass_email(**data)
    return jsonify(result), 201
   