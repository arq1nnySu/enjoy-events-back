from flask_jwt import JWT, jwt_required, _jwt
from apiRefactory import app, USERS

jwt = JWT(app)

@jwt.authentication_handler
def authenticate(username, password):
    return next((user for user in USERS if user.username == username and user.password == password), None)

@jwt.user_handler
def load_user(payload):
    if payload['user_id'] == 1:
        return User(id=1, username='cpi')

@jwt.payload_handler
def make_payload(user):
    return {
        'userId': user.id,
        'username': user.username
    }

def generate_token(user):
    """Generate a token for a user.
    """
    payload = _jwt.payload_callback(user)
    token = _jwt.encode_callback(payload)
    return {'token': token}
