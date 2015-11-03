from flask.ext.restplus import Resource
from api import api, VenueDC, log
from model.venue import Venue
from services.jwtService import *

ns = api.namespace('venues', description='Servicios para venues')

@ns.route('')
class VenuesService(Resource):
    @api.marshal_list_with(VenueDC)
    def get(self):
        return Venue.query.all()
