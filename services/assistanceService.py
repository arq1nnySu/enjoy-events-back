from flask.ext.restplus import Resource
from api import api, AssistancesDC, log, assistance_parser
from model.assistance import Assistance
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
        newAssistance = Assistance(
            eventTag = args.event,
            event = event.getAppearanceAssistance(),
            user = currentUser(),
            requirements = []
        )
        newAssistance.save()
        log.info("Crea una Asistencia con: {'evento':'%s'}" % newAssistance.event)
        return newAssistance, 201    
