def validate_user_data(data):
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    role = data.get('role', 'employee')

    if not username or not password or not email or not role:
        return {'error': 'username, password, email, and role are required and cannot be empty'}, 400
    return None

def validate_user_login(data):
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    if not username or not password or not email:
        return {'error': 'Username, password and email are required'},400
    return None

def validate_user_reset(data):
    username = data.get('username')
    current_password = data.get('current_password')
    new_password = data.get('new_password')
    if 'username' not in data or 'current_password' not in data or 'new_password' not in data:
        return {'error':'username, current_password and new_password are required'}, 400
    return None

def validate_user_forgot_password(data):
    email= data.get('email')
    if 'email' not in data:
        return {'error':'Email is required'}, 400
    return None

