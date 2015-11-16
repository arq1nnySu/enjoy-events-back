from flask.ext.restful.reqparse import RequestParser
from flask.ext.restplus import fields

# Documentacion de los eventos
class EventDocument(object):

	def __init__(self, api):
		self.api = api
		self.venueDocument = VenueDocument(api)
		self.event = self.create_event()
		self.events = self.create_events()
		self.parser = self.create_parser()
		self.error = self.create_error()

	def create_event(self):
		requirement = self.api.model('Requirement', {
			'name': fields.String(required=True, description='Event name'),
			'quantity': fields.Integer(required=True, description='Name of event')
			})
		visibility = self.api.model('Visibility', {
			'name': fields.String(required=True, description='Visibility name'),
			})
		event = self.api.model('Event', {
			'tag': fields.String(required=False, description='Tag of event'),
			'name': fields.String(required=True, description='Name of event'),
			'date': fields.String(required=True, description='Date of event'), # Cambiar el type por lo que corresponde.
			'time': fields.String(required=True, description='Time of event'),
			'capacity': fields.String(required=True, description='Capacity of event'),
			'venue': fields.Nested(self.venueDocument.venue, required=True, description='Venue of event'),
			'image': fields.String(required=True, description='Image of event'),
			'description': fields.String(required=True, description='Description of event'),
			'visibility': fields.Nested(visibility, required=True, description='Visibility of event'),
			'hasAssistance': fields.Boolean(required=False, description=''),
			'isOwner': fields.Boolean(required=False, description=''),
			'gests': fields.List(fields.String(), required=True, description='Description of event'),
			'requirementMissing': fields.List(fields.Nested(requirement), required=False, description='Requirements missing')
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
		parser.add_argument('venue', type=dict, required=True, help='Venue needs to be defined', location='json')
		parser.add_argument('image', type=str, required=True, help='Image needs to be defined', location='json')
		parser.add_argument('description', type=str, required=False, help='Description of event', location='json')
		parser.add_argument('visibility', type=dict, required=True, help='Visibility of event', location='json')
		parser.add_argument('gests', type=list, required=False, help='Gests of event', location='json'),
		parser.add_argument('capacity', type=int, required=True, help='Capacity of event', location='json')
		return parser

class VenueDocument(object):

	def __init__(self, api):
		self.api = api
		self.venue = self.create_venue()

	def create_venue(self):
		venue = self.api.model('Venue', {
			'name': fields.String(required=True, description='Name of venue'),
			'city': fields.String(required=True, description='City of venue'),
			'street': fields.String(required=True, description='Street of venue'),
			'country': fields.String(required=True, description='Country of venue'),
			})
		return venue

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
		parser.add_argument('password', type=str, required=False, help='Password needs to be defined', location='json')
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
		self.venueDocument = VenueDocument(api)
		self.requirement = self.create_requirement()
		self.assistanceEvent = self.create_assistanceEvent()
		self.assistance = self.create_assistance()
		self.assistances = self.create_assistances()
		self.parser = self.create_parser()

	def create_requirement(self):
		return self.api.model('Requirement', {
			'name': fields.String(required=True, description='Event name'),
			'quantity': fields.Integer(required=True, description='Name of event')
			})

	def create_assistance(self):
		return self.api.model('Assistance', {
			'event': fields.Nested(self.assistanceEvent, required=False, description='Evento'),
			'requirements': fields.Nested(self.requirement, required=False, description='Requerimientos')
			})

	def create_assistanceEvent(self):
		return self.api.model('AssistanceEvent', {
			'tag': fields.String(required=True, description='Event tag'),
			'name': fields.String(required=True, description='Event name'),
			'venue': fields.String(required=True, description='Event venue'),
			'time': fields.String(required=True, description='Event time'),
			'date': fields.String(required=True, description='Event date'),
			'image': fields.String(required=True, description='Event image')
			})

	def create_assistances(self):
		assistances = self.api.model('ListedAssistance', self.assistance)
		return assistances

	def create_parser(self):
		parser = RequestParser(bundle_errors=True)
		parser.add_argument('event', type=str, required=True, help='Event needs to be defined', location='json')
		parser.add_argument('requirements', type=list, required=False, help='Requirements (optional) needs to be defined', location='json')
		return parser


# Documentacion de las asistencias
class WatherDocument(object):
	def __init__(self, api):
		self.api = api
		self.parser = self.create_parser()

	def create_parser(self):
		parser = self.api.parser()
		parser.add_argument('event', type=str, help='Lugar')
		return parser
