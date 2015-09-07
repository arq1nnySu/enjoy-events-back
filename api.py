import os
from flask import Flask, request
from flask_jwt import JWT, jwt_required, _jwt
from flask.ext.restplus import Api, Resource, fields
from flask_cors import CORS

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app)
CORS(app)

api = Api(app, version='1.0', title='API',
    description='Api para el tp de arquitectura',
)

ns = api.namespace('events', description='Servicios para eventos')

class User(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

EVENTS = {
    "1":{'id': "1", 'name': 'Choripateada'},
    "2":{'id': "2", 'name': 'WISIT'},
    "3":{'id': "3", 'name': 'Lollapalooza'},
}


USERS = [
    User(id=1, username='cpi', password="unq")
]


event = api.model('Event', {
    'id': fields.String(required=False, description='Id of event'),
    'name': fields.String(required=True, description='Name of event')
})

events = api.model('ListedTodo', event)

def abort_if_event_doesnt_exist(event_id):
    if event_id not in EVENTS:
        api.abort(404, "Event {} doesn't exist".format(event_id))

parser = api.parser()
parser.add_argument('name', type=str, required=True, help='The name details', location='form')
parser.add_argument('id', type=str, required=False, help='The evnt id', location='form')


@ns.route('/<string:event_id>')
@api.doc(responses={404: 'Event not found', 401: 'Authorization Required'}, params={'event_id': 'The Todo ID'})
class EventService(Resource):
    @api.doc(description='event_id should be in {0}'.format(', '.join(EVENTS.keys())))
    @api.marshal_with(event)
    def get(self, event_id):
        abort_if_event_doesnt_exist(event_id)
        return EVENTS[event_id]

    # @jwt_required()
    @api.doc(responses={204: 'Event deleted'})
    def delete(self, event_id):
        abort_if_event_doesnt_exist(event_id)
        del EVENTS[event_id]
        return '', 204


@ns.route('/')
@api.doc(responses={401: 'Authorization Required'})
class EventListService(Resource):
    @api.marshal_list_with(events)
    def get(self):
        return [event for id, event in EVENTS.items()]

    @api.doc(parser=parser)
    # @jwt_required()
    @api.marshal_with(event, code=201)
    def post(self):
        args = parser.parse_args()
        event_id = '%d' % (len(EVENTS) + 1)
        EVENTS[event_id] = {'name': args['name'], "id":event_id}
        return EVENTS[event_id], 201


us = api.namespace('user', description='Servicios para usuario')

signup = api.model('Signup', {
    'username': fields.String(required=True, description='username'),
    'password': fields.String(required=True, description='password')
})

user_parser = api.parser()
user_parser.add_argument('username', type=str, required=True, help='El nombre del usuario', location='form')
user_parser.add_argument('password', type=str, required=True, help='La password', location='form')


@us.route('')
class UserService(Resource):
    @api.marshal_list_with(events)
    @jwt.user_handler
    def get(self):
        return next((user for user in USERS if user.username == username), None)

    @api.doc(parser=user_parser)
    def post(self):
        args = user_parser.parse_args()
        user_id = '%d' % (len(USERS) + 1)
        user = User(id=user_id, username=args['username'], password=args['password'])
        USERS.append(user)
        return generate_token(user), 201


def generate_token(user):
    """Generate a token for a user.
    """
    payload = _jwt.payload_callback(user)
    token = _jwt.encode_callback(payload)
    return {'token': token}


@jwt.authentication_handler
def authenticate(username, password):
    return next((user for user in USERS if user.username == username and user.password == password), None)

@jwt.user_handler
def load_user(payload):
    if payload['user_id'] == 1:
        return User(id=1, username='cpi')

@jwt.payload_handler
def make_payload(user):
    return {
        'userId': user.id,
        'username': user.username
    }

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
