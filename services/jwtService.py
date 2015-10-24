from flask_jwt import JWT, _jwt, current_identity, JWTError, _jwt_required
from flask import request, _request_ctx_stack
from functools import wraps
from api import app, api, log
from model.user import User


def authenticate(username, password):
    log.info("Autenticar Usuario: {'username':'%s'}" % username)
    db_user = User.query.get_by_name(username)
    if db_user is not None and db_user.check_password(password):
        return db_user
    return None



def identity(payload):
    log.info("Cargar Usuario: {'username':'%s'}" % payload['username'])
    user = User.query.get_by_name(payload['username'])
    return user

jwt = JWT(app, authenticate, identity)

@jwt.jwt_payload_handler
def make_payload(user):
    return {'username': user.username, 'email':user.email}


def generate_token(user):
    log.info("Generar Token para un Usuario: {'user':'%s'}" % user)
    payload = _jwt.jwt_payload_callback(user)
    token = _jwt.jwt_encode_callback(user)
    return {'access_token': token}


def jwt_optional(realm=None):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            optional_jwt(realm)
            return fn(*args, **kwargs)

        return decorator

    return wrapper

def jwt_required(realm=None):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            _jwt_required(realm)
            return fn(*args, **kwargs)

        return decorator

    return wrapper

@jwt.jwt_error_handler
def error_handler(e):
    api.abort(401, "Authorization Required")


def currentUser():
    return _request_ctx_stack.top.current_identity


def isLogged():
    return currentUser() is not None


def optional_jwt(realm=None):
    try:
        _jwt_required(realm)
    except JWTError:
        _request_ctx_stack.top.current_identity = None


