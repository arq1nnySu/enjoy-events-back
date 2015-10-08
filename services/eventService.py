from api import api, EVENTS, EventsDC, EventDC, ErrorDC, event_parser
from flask.ext.restplus import Resource
from model.event import Event
from model.visibility import Visibility
from services.jwtService import *
from flask_jwt import jwt_required
from log.logger import getLogger

log = getLogger()

ns = api.namespace('events', description='Servicios para eventos')

@ns.route('/<string:tag>')
@api.doc(responses={404: 'Event not found', 401: 'Authorization Required'}, params={'tag': 'Tag\'s Event'})
class EventService(Resource):
    @api.marshal_with(EventDC)
    @jwt_optional()
    def get(self, tag):
        log.info("Devuelve un evento con: {'tag':'%s'}" % tag)
        event = Event.query.get_by_tag(tag)
        if event.hasAccess(currentUser()) :
            return event
        else:
            api.abort(401, "Authorization Required")

    @jwt_required()
    @api.doc(responses={204: 'Event deleted'})
    def delete(self, tag):
        log.info("Elimina un evento con: {'tag':'%s'}" % tag)
        eventToDelete = Event.query.get_by_tag(tag)
        eventToDelete.delete()
        return '', 204

@ns.route('/')
@api.doc(responses={401: 'Authorization Required'})
class EventListService(Resource):            
    @api.marshal_list_with(EventsDC)
    @jwt_optional()
    def get(self):
        log.info("Devuelve todos los eventos con filtrado.")        
        if isLogged() :
            return Event.query.filter((Event.visibility == Visibility.query.public()).or_(
                Event.owner == currentUser()).or_(Event.gests.in_(currentUser()))
                ).all()
        else:
            return Event.query.filter(Event.visibility == Visibility.query.public()).all()


    @api.doc(parser=event_parser)
    @jwt_required()
    @api.marshal_with(EventDC, code=201)
    def post(self):
        args = event_parser.parse_args()
        newEvent = Event(
            tag = args.tag,
            name = args.name,
            description = args.description,
            venue = args.venue,
            time = args.time,
            date = args.date,
            image = args.image,
            gests = [],
            visibility = Visibility.query.get(args.visibility),
            owner = currentUser()
        )
        newEvent.save()
        log.info("Crea un nuevo evento con: {'tag':'%s'}" % newEvent.tag)
        return newEvent, 201


