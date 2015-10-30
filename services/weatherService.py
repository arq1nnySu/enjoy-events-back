from flask.ext.restplus import Resource
import requests
import requests_cache

from api import api
from services.jwtService import login_optional

ws = api.namespace('weather', description='Servicios para el clima')

# expires_after is seconds (7200 is 2 hours)
requests_cache.install_cache(cache_name='demo_cache', backend='memory', expire_after=7200)


@ws.route('')
@api.doc()
class WeatherService(Resource):
    @login_optional()
    def get(self):
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Bernal, ar&mode=json&units=metric&cnt=1&appid=bd82977b86bf27fb59a04b61b657fb6f&lang=es')
        response = r.json()
        response["main"]
        main= response["main"]
        return {
        	"coord": response["coord"],
        	"weather": response["weather"][0], 
        	"data": {
        		"temperature": ('%2.0f' % main["temp"]),
        		"pressure": main["pressure"],
        		"humidity": main["humidity"],
        		"wind": response["wind"]["speed"]
        	}
        }
