from api import api, EVENTS, events, event, event_parser
from flask.ext.restplus import Resource

ns = api.namespace('events', description='Servicios para eventos')

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

    @api.doc(parser=event_parser)
    # @jwt_required()
    @api.marshal_with(event, code=201)
    def post(self):
        args = event_parser.parse_args()
        event_id = '%d' % (len(EVENTS) + 1)
        EVENTS[event_id] = {'name': args['name'], "id":event_id}
        return EVENTS[event_id], 201

def abort_if_event_doesnt_exist(event_id):
    if event_id not in EVENTS:
        api.abort(404, "Event {} doesn't exist".format(event_id))

