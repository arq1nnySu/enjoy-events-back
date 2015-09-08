import os
from flask import Flask, request
from flask.ext.restplus import Api
from model.user import User
from docs.app import UserDocument, EventDocument

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

api = Api(app, version='1.0', title='API',
    description='Api para el tp de arquitectura',
)

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

@app.after_request
def add_cors_headers(response):
    if 'Origin' in request.headers:
        response.headers.add('Access-Control-Allow-Origin', request.headers.get('Origin'))
        response.headers.add('Access-Control-Allow-Credentials', 'true')

        if 'Access-Control-Request-Methods' in request.headers:
            response.headers.add('Access-Control-Allow-Methods', request.headers.get('Access-Control-Request-Methods'))

        if 'Access-Control-Request-Headers' in request.headers:
            response.headers.add('Access-Control-Allow-Headers', request.headers.get('Access-Control-Request-Headers'))

    return response


