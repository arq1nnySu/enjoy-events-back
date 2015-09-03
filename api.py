from flask import Flask, request
from flask_jwt import JWT, jwt_required
from flask.ext.restplus import Api, Resource, fields

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app)

api = Api(app, version='1.0', title='API',
    description='Api para el tp de arquitectura',
)

ns = api.namespace('events', description='Servicios para eventos')

EVENTS = {
        "1":{'id': "1", 'name': 'Choripateada'},
        "2":{'id': "2", 'name': 'WISIT'},
        "3":{'id': "3", 'name': 'Lollapalooza'},
}

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



class User(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

us = api.namespace('user', description='Servicios para usuario')

sigin = api.model('Sigin', {
    'username': fields.String(required=False, description='username'),
    'token': fields.String(required=True, description='token')
})


@jwt.authentication_handler
def authenticate(username, password):
    if username == 'cpi' and password == 'unq':
        return User(id=1, username=username)

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


# Chequeando que todo ande bien


if __name__ == '__main__':
    app.run(debug=True)
   print "Haciendo prueba para ver si funciona la integracion con pivotal :)" 