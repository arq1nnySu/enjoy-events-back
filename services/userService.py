from flask.ext.restplus import Resource

from api import api, events, user_parser
from services.jwtService import jwt, generate_token
from model.user import User

us = api.namespace('user', description='Servicios para usuario')


@us.route('')
class UserService(Resource):        
    @api.marshal_list_with(events)
    @jwt.user_handler
    def get(self):
        return User.query.get_by_name(username).first()

    @api.doc(parser=user_parser)
    def post(self):
        args = user_parser.parse_args()
        user = User(username=args['username'], password=args['password'])
        user.save()
        return generate_token(user), 201


