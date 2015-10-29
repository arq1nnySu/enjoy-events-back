from api import api, EventsDC, EventDC, ErrorDC, event_parser, log
from flask.ext.restplus import Resource
from model.event import Event
from model.visibility import Visibility
from services.jwtService import *

ns = api.namespace('events', description='Servicios para eventos')

@ns.route('/<string:tag>')
@api.doc(responses={404: 'Event not found', 401: 'Authorization Required'}, params={'tag': 'Tag\'s Event'})
class EventService(Resource):
    @api.marshal_with(EventDC)
    @login_optional()
    def get(self, tag):
        log.info("Otorga el Evento con: {'tag':'%s'}" % tag)
        event = Event.query.get_by_tag(tag)
        if event.hasAccess(currentUser()) :
            return event
        else:
            log.warning("Se requiere Autorizacion para este recurso.")
            api.abort(401, "Authorization Required")

    @login_required()
    @api.doc(responses={204: 'Event deleted'})
    def delete(self, tag):
        log.info("Elimina un Evento con: {'tag':'%s'}" % tag)
        eventToDelete = Event.query.get_by_tag(tag)
        eventToDelete.delete()
        return '', 204

@ns.route('/')
@api.doc(responses={401: 'Authorization Required'})
class EventListService(Resource):            
    @api.marshal_list_with(EventsDC)
    @login_optional()
    def get(self):
        log.info("Lista los Eventos. En estado Publico o Privado.")        
        if isLogged() :
            return Event.query.filter((Event.visibility == Visibility.query.public()).or_(
                Event.owner == currentUser()).or_(Event.gests.in_(currentUser().username))
                ).all()
        else:
            return Event.query.filter(Event.visibility == Visibility.query.public()).all()

    @api.doc(parser=event_parser)
    @login_required()
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
            gests = args.gests,
            requirement = [],
            capacity = args.capacity,
            visibility = Visibility.query.get(args.visibility),
            owner = currentUser()
        )
        newEvent.save()
        log.info("Crea un Evento con: {'tag':'%s'}" % newEvent.tag)
        return newEvent, 201
