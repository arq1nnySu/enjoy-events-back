from flask_jwt import JWT, _jwt

from api import app
from model.user import User

jwt = JWT(app)


@jwt.authentication_handler
def authenticate(username, password):
    return User.query.get_by_name_and_password(username, password).first()


@jwt.user_handler
def load_user(payload):
    if payload['user_id'] == 1:
        return User(username='cpi')


@jwt.payload_handler
def make_payload(user):
    return {
        'username': user.username
    }


def generate_token(user):
    """Generate a token for a user.
    """
    payload = _jwt.payload_callback(user)
    token = _jwt.encode_callback(payload)
    return {'token': token}
