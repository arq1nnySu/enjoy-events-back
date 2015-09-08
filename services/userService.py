from api import api, USERS, events, user_parser
from services.jwtService import jwt, generate_token
from flask.ext.restplus import Resource
from docs.app import UserDocument 

us = api.namespace('user', description='Servicios para usuario')

@us.route('')
class UserService(Resource):        
    @api.marshal_list_with(events)
    @jwt.user_handler
    def get(self):
        return next((user for user in USERS if user.username == username), None)

    @api.doc(parser=user_parser)
    def post(self):
        args = user_parser.parse_args()
        user_id = '%d' % (len(USERS) + 1)
        user = User(id=user_id, username=args['username'], password=args['password'])
        USERS.append(user)
        return generate_token(user), 201


