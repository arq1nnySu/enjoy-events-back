from flask.ext.restplus import fields 

# Documentacion de los eventos
class EventDocument(object):

	def __init__(self, api):
		self.api = api
		self.event = self.create_event()
		self.events = self.create_events()
		self.parser = self.create_parser()

	def create_event(self):
		event = self.api.model('Event', {
			'id': fields.String(required=False, description='Id of event'),
			'name': fields.String(required=True, description='Name of event'),
			'date': fields.String(required=True, description='Date of event'), # Cambiar el type por lo que corresponde.
			'time': fields.String(required=True, description='Time of event'), 
			'venue': fields.String(required=True, description='Venue of event'),
			'description': fields.String(required=True, description='Description of event')
			})
		return event

	def create_events(self):
		events = self.api.model('ListedTodo', self.event)
		return events

	def create_parser(self):
		parser = self.api.parser()
		parser.add_argument('id', type=str, required=False, help='The evnt id', location='form')
		parser.add_argument('name', type=str, required=True, help='The name details', location='form')
		parser.add_argument('date', type=str, required=True, help='The Date', location='form') # Cambiar el type por lo que corresponde.
		parser.add_argument('time', type=str, required=False, help='The Time', location='form') # Cambiar el type por lo que corresponde.
		parser.add_argument('venue', type=str, required=True, help='The Venue', location='form')
		parser.add_argument('description', type=str, required=False, help='The Description', location='form')
		return parser

#Documentacion de los usuarios
class UserDocument(object):

	def __init__(self, api):
		self.api = api
		self.parser = self.create_parser()
		self.signup = self.create_signup()

	def create_parser(self):
		parser = self.api.parser()
		parser.add_argument('username', type=str, required=True, help='El nombre del usuario', location='form')
		parser.add_argument('password', type=str, required=True, help='La password', location='form')
		return parser

	def create_signup(self):
		signup = self.api.model('Signup', 
			{ 'username': fields.String(required=True, description='username'),
			  'password': fields.String(required=True, description='password')
			})
