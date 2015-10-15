from flask.ext.restplus import Resource
from api import api, AssistancesDC, log
from model.assistance import Assistance
from model.user import User
from services.jwtService import *
from flask_jwt import jwt_required

ns = api.namespace('assistance', description='Servicios para asistencias')

@ns.route('')
class AssistanceService(Resource):
    @api.marshal_list_with(AssistancesDC)
    # @jwt_required()
    def get(self):
        return Assistance.query.get_by_user(User.query.get_by_name('cpi'))
