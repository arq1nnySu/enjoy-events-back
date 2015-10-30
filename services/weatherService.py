from flask.ext.restplus import Resource

from api import api
from services.jwtService import login_optional
import requests

ws = api.namespace('weather', description='Servicios para el clima')


@ws.route('')
@api.doc()
class WeatherService(Resource):
    @login_optional()
    def get(self):
        r = requests.get('http://api.aerisapi.com/observations/seattle,wa?client_id=9WB9QIwFrDLrYgsINtYpF&client_secret=L8GcaqJ6ZYmqVqVHSzFRl43DsNI3LMfwfL0WmXOG')
        return r.json()
