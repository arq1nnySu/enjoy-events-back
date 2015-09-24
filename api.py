import os
from flask import Flask
from flask.ext.restplus import Api, RestException
from flask_cors import CORS
from model.user import User
from model.event import Event
from docs.app import UserDocument, EventDocument

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['RESTPLUS_VALIDATE'] = True

CORS(app)


errors = {
    'SpecsError': {
        'message': "This field can't be empty.",
        'status': 400,
    },
    'ValidationError': {
        'message': "This field can't be empty.",
        'status': 400,
    },
    'RestException': {
        'message': "This field can't be empty.",
        'status': 400,
    }
}

api = Api(app, version='1.0', title='API',
    description='Api para el tp de arquitectura',errors=errors)


@api.errorhandler(Exception)
def handle_custom_exception(error):
    return {'message': 'What you want'}, 400

EVENTS = {
    "1": Event({'id': "1", 'name': 'Choripateada'}),
    "2":Event({'id': "2", 'name': 'WISIT'}),
    "3":Event({'id': "3", 'name': 'Lollapalooza'}),
}

ed = EventDocument(api)

event = ed.event

events = ed.events

event_parser = ed.parser


USERS = [
    User(id=1, username='cpi', password="unq")
]

ud = UserDocument(api)

user_parser = ud.parser

signup = ud.signup
