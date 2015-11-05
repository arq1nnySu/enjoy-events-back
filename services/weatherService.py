from flask.ext.restplus import Resource
import requests
import requests_cache
from datetime import datetime
from api import api, wather_parser, log
from services.jwtService import login_optional
from model.event import Event

ws = api.namespace('weather', description='Servicios para el clima')

# expires_after is seconds (7200 is 2 hours)
requests_cache.install_cache(cache_name='demo_cache', backend='memory', expire_after=7200)


@ws.route('')
@api.doc()
class WeatherService(Resource):
    @login_optional()
    @api.doc(parser=wather_parser)
    def get(self):
        args = wather_parser.parse_args()
        event = Event.query.get_by_tag(args.event)

        eventDate = datetime.strptime(event.date, "%Y-%m-%d")
        today = datetime.today()
        days = (eventDate - today).days

        if days <= 16 :
            place = "{0}, {1}, {2}".format(event.venue.street, event.venue.city, event.venue.country) 
            r = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=${0}&mode=json&units=metric&cnt=${1}&appid=5bb6740af88caf0f0825477ff473c661&lang=en'.format(place, days))
            response = r.json()
            if 200 <= r.status_code < 300:
                data = response["list"][days-1]
                main = data["main"]
                return {
                    "coord": response["city"]["coord"],
                    "weather": data["weather"][0],
                    "data": {
                        "temperature": ('%2.0f' % main["temp"]),
                        "pressure": main["pressure"],
                        "humidity": main["humidity"],
                        "wind": data["wind"]["speed"]
                    }
                }
        return {}
