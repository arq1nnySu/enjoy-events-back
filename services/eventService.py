from flask.ext.restful.reqparse import RequestParser
from api import api, EventsDC, EventDC, ErrorDC, event_parser, log
from flask.ext.restplus import Resource
from flask import request
from model.event import Event
from model.venue import Venue
from model.visibility import Visibility
from model.assistance import Assistance
from services.jwtService import *
from model.user import User

ns = api.namespace('events', description='Servicios para eventos')

@ns.route('/<string:tag>')
@api.doc(responses={404: 'Event not found', 401: 'Authorization Required'}, params={'tag': 'Tag\'s Event'})
class EventService(Resource):
    @api.marshal_with(EventDC)
    @login_optional()
    def get(self, tag):
        log.info("Otorga el Evento con: {'tag':'%s'}" % tag)
        event = Event.query.get_by_tag(tag)
        event.hasAssistance = False
        event.isOwner= False
        if isLogged():
            user = currentUser()
            if event.hasAccess(user) :
                assistance = Assistance.query.get_by_eventTag_and_user(event, user)
                event.hasAssistance = assistance is not None
                event.requirementMissing = event.lackRequirements()
                event.isOwner = event.owner.username == user.username
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


removeEventParser = RequestParser(bundle_errors=True)
removeEventParser.add_argument('tag', type=str, required=True, help='Tag of event', location='json')

@ns.route('')
@api.doc(responses={401: 'Authorization Required'})
class EventListService(Resource):            
    @api.marshal_list_with(EventsDC)
    @login_optional()
    def get(self):
        log.info("Lista los Eventos. En estado Publico o Privado.")        
        page = int(request.args.get('page', 1))
        if isLogged() :
            return Event.query.filter((Event.visibility == Visibility.query.public()).or_(
                Event.owner == currentUser()).or_(Event.gests.in_(currentUser().username))
                ).ascending(Event.date).paginate(page, 15).items
        else:
            return Event.query.filter(Event.visibility == Visibility.query.public()).ascending(Event.date).paginate(page, 15).items

    @api.doc(parser=event_parser)
    @login_required()
    @api.marshal_with(EventDC, code=201)
    def post(self):
        args = event_parser.parse_args()
        newEvent = Event(
            tag = args.tag,
            name = args.name,
            description = args.description,
            venue = Venue.query.get_by_name(args.venue["name"]),
            time = args.time,
            date = args.date,
            image = args.image,
            gests = map(lambda gest: gest["username"], args.gests),
            requirement = map(lambda req: Requirement(name=req["name"],quantity=req["quantity"]), args.requirement),
            capacity = args.capacity,
            visibility = Visibility.query.get(args.visibility),
            owner = currentUser()
        )
        newEvent.save()
        log.info("Crea un Evento con: {'tag':'%s'}" % newEvent.tag)
        return newEvent, 201

    @api.doc(parser=event_parser)
    @login_required()
    @api.marshal_with(EventDC, code=201)
    def put(self):
        args = event_parser.parse_args()
        event = Event.query.get_by_tag(args.tag)
        event.name = args.name
        event.description = args.description
        event.venue = Venue.query.get_by_name(args.venue["name"])
        event.time = args.time
        event.date = args.date
        event.image = args.image
        event.gests = map(lambda gest: gest["username"], args.gests)
        event.requirement = []
        event.capacity = args.capacity
        event.visibility = Visibility.query.get(args.visibility["name"])

        event.save()
        log.info("Edita un Evento con: {'tag':'%s'}" % event.tag)
        return event, 201

    @api.doc(parser=removeEventParser)
    @login_required()
    def delete(self):
        args = removeEventParser.parse_args()
        event = Event.query.get_by_tag(args.tag)

        Assistance.query.removeFromEventTag(event.tag)

        event.remove()
        log.info("Elimina un Evento con: {'tag':'%s'}" % event.tag)
        return {}, 201
