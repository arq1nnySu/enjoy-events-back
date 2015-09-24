from api import api, EVENTS, events, event, event_parser
from flask.ext.restplus import Resource
from model.event import Event

ns = api.namespace('events', description='Servicios para eventos')

@ns.route('/<string:tag>')
@api.doc(responses={404: 'Event not found', 401: 'Authorization Required'}, params={'tag': 'Tag\'s Event'})
class EventService(Resource):
    @api.doc(description='')
    @api.marshal_with(event)
    def get(self, tag):
        return Event.query.filter(Event.tag == tag).first()

    # @jwt_required()
    @api.doc(responses={204: 'Event deleted'})
    def delete(self, event_id):
        # abort_if_event_doesnt_exist(event_id)
        eventToDelete = Event.query.filter(Event.tag == tag).first()
        eventToDelete.delete()
        return '', 204

@ns.route('/')
@api.doc(responses={401: 'Authorization Required'})
class EventListService(Resource):            
    @api.marshal_list_with(events)
    def get(self):
        return Event.query.all()

    @api.doc(parser=event_parser)
    # @jwt_required()
    @api.marshal_with(event, code=201)
    @api.response(400, 'Validation Error')
    def post(self):
        args = event_parser.parse_args()
        newEvent = Event(
            tag = args.tag,
            name = args.name,
            description = args.description,
            venue = args.venue,
            time = args.time,
            date = args.date,
            image = args.image
        )
        newEvent.save()
        return newEvent, 201


