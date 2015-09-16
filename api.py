import os
from flask import Flask
from flask.ext.restplus import Api
from flask_cors import CORS
from model.user import User
from model.event import Event
from docs.app import UserDocument, EventDocument

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

CORS(app)

api = Api(app, version='1.0', title='API',
    description='Api para el tp de arquitectura',
)

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
