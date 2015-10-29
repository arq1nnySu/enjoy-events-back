from flask.ext.restplus import Resource
from api import api, AssistancesDC, log
from model.assistance import Assistance
from model.user import User
from services.jwtService import *

ns = api.namespace('assistances', description='Servicios para asistencias')

@ns.route('')
class AssistanceService(Resource):
    @api.marshal_list_with(AssistancesDC)
    @login_required()
    def get(self):
        return Assistance.query.get_by_user(currentUser())
