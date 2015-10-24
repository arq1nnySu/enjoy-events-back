from flask.ext.restful.reqparse import RequestParser
from flask.ext.restplus import fields

# Documentacion de los eventos
class EventDocument(object):

	def __init__(self, api):
		self.api = api
		self.event = self.create_event()
		self.events = self.create_events()
		self.parser = self.create_parser()
		self.error = self.create_error()

	def create_event(self):
		event = self.api.model('Event', {
			'tag': fields.String(required=False, description='Tag of event'),
			'name': fields.String(required=True, description='Name of event'),
			'date': fields.String(required=True, description='Date of event'), # Cambiar el type por lo que corresponde.
			'time': fields.String(required=True, description='Time of event'),
			'venue': fields.String(required=True, description='Venue of event'),
			'image': fields.String(required=True, description='Image of event'),
			'description': fields.String(required=True, description='Description of event'),
			'gests': fields.List(fields.String(), required=True, description='Description of event')
			})
		return event

	def create_events(self):
		events = self.api.model('ListedTodo', self.event)
		return events

	def create_error(self):
		error = self.api.model('Error', {
			'message': fields.String(required=False)
		})
		return error

	def create_parser(self):
		parser = RequestParser(bundle_errors=True)
		parser.add_argument('tag', type=str, required=True, help='Tag of event', location='json')
		parser.add_argument('name', type=str, required=True, help='Name needs to be defined', location='json')
		parser.add_argument('date', type=str, required=True, help='Date needs to be defined', location='json') # Cambiar el type por lo que corresponde.
		parser.add_argument('time', type=str, required=False, help='Time of event', location='json') # Cambiar el type por lo que corresponde.
		parser.add_argument('venue', type=str, required=True, help='Venue needs to be defined', location='json')
		parser.add_argument('image', type=str, required=True, help='Image needs to be defined', location='json')
		parser.add_argument('description', type=str, required=False, help='Description of event', location='json')
		parser.add_argument('visibility', type=str, required=True, help='Visibility of event', location='json')
		parser.add_argument('gests', type=list, required=False, help='Gests of event', location='json'),
		parser.add_argument('capacity', type=int, required=True, help='Capacity of event', location='json')
		return parser

#Documentacion de los usuarios
class UserDocument(object):

	def __init__(self, api):
		self.api = api
		self.parser = self.create_parser()
		self.signup = self.create_signup()
		self.users = self.create_users()

	def create_signup(self):
		signup = self.api.model('Signup', 
			{ 'username': fields.String(required=True, description='Username'),
			  'email': fields.String(required=True, description='Email'),
			  'firstName': fields.String(required=False, description='FirstName'),
			  'lastName': fields.String(required=False, description='LastName'),
			  'phone': fields.String(required=False, description='Phone'),
			})
		return signup

	def create_parser(self):
		parser = RequestParser(bundle_errors=True)
		parser.add_argument('username', type=str, required=True, help='Name needs to be defined', location='json')
		parser.add_argument('password', type=str, required=True, help='Password needs to be defined', location='json')
		parser.add_argument('email', type=str, required=True, help='Email needs to be defined', location='json')
		parser.add_argument('firstName', type=str, required=False, location='json')
		parser.add_argument('lastName', type=str, required=False, location='json')
		parser.add_argument('phone', type=str, required=False, location='json')
		return parser

	def create_users(self):
		users = self.api.model('ListUsers', self.signup)
		return users


#Documentacion de las asistencias
class AssistanceDocument(object):

	def __init__(self, api, eventDC):
		self.api = api
		self.eventDC = eventDC
		self.requirement = self.create_requirement()
		self.assistance = self.create_assistance()
		self.assistances = self.create_assistances()

	def create_requirement(self):
		return self.api.model('Requirement', {
			'name': fields.String(required=True, description='Event name'),
			'quantity': fields.Integer(required=True, description='Name of event')
			})

	def create_assistance(self):
		return self.api.model('Assistance', {
			'event': fields.Nested(self.eventDC.event, required=False, description='Evento'),
			'requirements': fields.Nested(self.requirement, required=False, description='Requerimientos')
			})

	def create_assistances(self):
		assistances = self.api.model('ListedAssistance', self.assistance)
		return assistances

