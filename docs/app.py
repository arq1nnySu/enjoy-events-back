from flask.ext.restplus import fields 
#from flask_restful.reqparse import RequestParser
from flask.ext.restful.reqparse import RequestParser

# Documentacion de los eventos
class EventDocument(object):

	def __init__(self, api):
		self.api = api
		self.event = self.create_event()
		self.events = self.create_events()
		self.parser = self.create_parser()

	def create_event(self):
		event = self.api.model('Event', {
			'id': fields.String(required=False, description='Id'),
			'name': fields.String(required=True, description='Name'),
			'date': fields.String(required=True, description='Date'), # Cambiar el type por lo que corresponde.
			'time': fields.String(required=False, description='Time'), 
			'venue': fields.String(required=True, description='Venue'),
			'description': fields.String(required=False, description='Description')
			})
		return event

	def create_events(self):
		events = self.api.model('ListedTodo', self.event)
		return events

	def create_parser(self):
		parser = RequestParser(bundle_errors=True)
		parser.add_argument('id', type=str, required=False, help='Id of event', location='form')
		parser.add_argument('name', type=str, required=True, help='Name needs to be defined', location='form')
		parser.add_argument('date', type=str, required=True, help='Date needs to be defined', location='form') # Cambiar el type por lo que corresponde.
		parser.add_argument('time', type=str, required=False, help='Time of event', location='form') # Cambiar el type por lo que corresponde.
		parser.add_argument('venue', type=str, required=True, help='Venue needs to be defined', location='form')
		parser.add_argument('description', type=str, required=False, help='Description of event', location='form')
		return parser

#Documentacion de los usuarios
class UserDocument(object):

	def __init__(self, api):
		self.api = api
		self.parser = self.create_parser()
		self.signup = self.create_signup()

	def create_signup(self):
		signup = self.api.model('Signup', 
			{ 'username': fields.String(required=True, description='Username'),
			  'password': fields.String(required=True, description='Password')
			})

	def create_parser(self):
		parser = RequestParser(bundle_errors=True)
		parser.add_argument('username', type=str, required=True, help='Name needs to be defined', location='form')
		parser.add_argument('password', type=str, required=True, help='Password needs to be defined', location='form')
		return parser

