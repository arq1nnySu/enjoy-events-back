import os
from flask import Flask
from flask.ext.restplus import Api, RestException
from flask_cors import CORS
from urlparse import urlsplit
from flask.ext.mongoalchemy import MongoAlchemy
from docs.app import UserDocument, EventDocument, AssistanceDocument, WatherDocument, VenueDocument
from datetime import timedelta
from log.logger import getLogger
from services.MailService import MailService
log = getLogger()

app = Flask(__name__)
app.debug = True
# Configuracion de app.
app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_REQUIRED_CLAIMS'] = []
app.config['JWT_EXPIRATION_DELTA'] =  timedelta(hours=12)
app.config['BUNDLE_ERRORS'] = True

# Configuracion de MongoDB.
url = os.environ.get('MONGOLAB_URI', 'mongodb://localhost/enjoy-events')
app.config['MONGOALCHEMY_CONNECTION_STRING'] = url
parsed = urlsplit(url)
app.config['MONGOALCHEMY_DATABASE'] = parsed.path[1:]
db = MongoAlchemy(app)


CORS(app)


errors = {
   'SpecsError': {
       'message': "This field can't be empty.",
       'status': 401,
   },
   'ValidationError': {
       'message': "This field can't be empty.",
       'status': 402,
   },
   'RestException': {
       'message': "This field can't be empty.",
       'status': 400,
   }
}

api = Api(app, version='1.0', title='API',
    description='Api para el tp de arquitectura', errors=errors)


#@api.errorhandler(Exception)
#def handle_custom_exception(error):
#    return {'message': 'What you want'}, 400

ed = EventDocument(api)

EventDC = ed.event
ErrorDC = ed.error

EventsDC = ed.events

ad = AssistanceDocument(api, ed)

AssistanceDC = ad.assistance
AssistancesDC = ad.assistances

assistance_parser = ad.parser

event_parser = ed.parser

ud = UserDocument(api)

UsersDC = ud.users
signup = ud.signup

user_parser = ud.parser

wd = WatherDocument(api)
wather_parser = wd.parser

vd = VenueDocument(api)
VenueDC = vd.venue

mailService = MailService(app)

@app.route('/bootstrap')
def bootstrap():
  from bootstrap import development
  development()
  return 'OK'