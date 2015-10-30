from flask.ext.restplus import Resource
import requests
import requests_cache

from api import api
from services.jwtService import login_optional

ws = api.namespace('weather', description='Servicios para el clima')

# expires_after is seconds (7200 is 2 hours)
requests_cache.install_cache(cache_name='demo_cache', expire_after=7200)


@ws.route('')
@api.doc()
class WeatherService(Resource):
    @login_optional()
    def get(self):
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Bernal,ar&lang=es&appid=bd82977b86bf27fb59a04b61b657fb6f')
        return r.json()
