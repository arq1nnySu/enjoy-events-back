import os
from flask import Flask
from flask.ext.restplus import Api, RestException
from flask_cors import CORS
from flask.ext.mongoalchemy import MongoAlchemy
from docs.app import UserDocument, EventDocument

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['RESTPLUS_VALIDATE'] = True

app.config['MONGOALCHEMY_DATABASE'] = 'enjoy-events'
app.config['MONGOALCHEMY_CONNECTION_STRING'] = os.environ.get('MONGOLAB_URI', 'mongodb://localhost/enjoy-events')
db = MongoAlchemy(app)

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

EVENTS = {}

ed = EventDocument(api)

event = ed.event

events = ed.events

event_parser = ed.parser

ud = UserDocument(api)

user_parser = ud.parser

signup = ud.signup
