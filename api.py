import os
from flask import Flask
from flask.ext.restplus import Api
from flask_cors import CORS
from model.user import User
from docs.app import UserDocument, EventDocument

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

api = Api(app, version='1.0', title='API',
    description='Api para el tp de arquitectura',
)

CORS(app)

EVENTS = {
    "1":{'id': "1", 'name': 'Choripateada'},
    "2":{'id': "2", 'name': 'WISIT'},
    "3":{'id': "3", 'name': 'Lollapalooza'},
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
