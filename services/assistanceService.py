from flask.ext.restplus import Resource
from api import api, AssistancesDC, log, assistance_parser, mailService
from model.assistance import Assistance, Requirement
from model.user import User
from model.event import Event
from services.jwtService import *

ns = api.namespace('assistances', description='Servicios para asistencias')

@ns.route('')
class AssistanceService(Resource):
    @api.marshal_list_with(AssistancesDC)
    @login_required()
    def get(self):
        return Assistance.query.get_by_user(currentUser())

    @api.doc(parser=assistance_parser)
    @api.marshal_with(AssistancesDC, code=201)
    @login_required()
    def post(self):
        args = assistance_parser.parse_args()
        event = Event.query.get_by_tag(args.event)
        if not event.hasAvailability():
            api.abort(400, "The event haven't availability")

        newAssistance = Assistance(
            eventTag = args.event,
            event = event.getAppearanceAssistance(),
            user = currentUser().username,
            requirements = map(lambda req: Requirement(name=req["name"],quantity=req["quantity"]), args.requirements)
        )
        newAssistance.save()
        mailService.assistance(newAssistance, currentUser())
        log.info("Crea una Asistencia con: {'evento':'%s'}" % newAssistance.event)
        return newAssistance, 201    

    @api.doc(parser=assistance_parser)
    @login_required()
    def delete(self):
        args = assistance_parser.parse_args()
        assistance = Assistance.query.get_by_eventTag_and_user(args.event, currentUser())
        assistance.remove()
        return '', 204