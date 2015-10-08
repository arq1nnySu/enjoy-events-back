from flask_jwt import JWT, _jwt, current_user, JWTError, verify_jwt
from flask import request, _request_ctx_stack
from functools import wraps
from api import app, api, log
from model.user import User

jwt = JWT(app)

@jwt.authentication_handler
def authenticate(username, password):
    log.info("Autenticar Usuario: {'username':'%s'}" % username)
    return User.query.get_by_name_and_password(username, password).first()

@jwt.user_handler
def load_user(payload):
    logger.info("Cargar Usuario: {'username':'%s'}" % payload['username'])
    return User.query.get_by_name(payload['username']).first()

@jwt.payload_handler
def make_payload(user):
    return {'username': user.username}

def generate_token(user):
    log.info("Generar Token para un Usuario: {'user':'%s'}" % user)
    payload = _jwt.payload_callback(user)
    token = _jwt.encode_callback(payload)
    return {'token': token}

def jwt_optional(realm=None):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            optional_jwt(realm)
            return fn(*args, **kwargs)
        return decorator
    return wrapper
    
@jwt.error_handler
def error_handler(e):
    api.abort(401, "Authorization Required")

def currentUser():
    return _request_ctx_stack.top.current_user

def isLogged():
    return currentUser() != None

def optional_jwt(realm=None):
    try:
        verify_jwt(realm)
    except JWTError:
        _request_ctx_stack.top.current_user = None
        