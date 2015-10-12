from flask.ext.restplus import Resource
from api import api, signup, user_parser, log
from services.jwtService import jwt, generate_token
from model.user import User

us = api.namespace('user', description='Servicios para usuario')

@us.route('')
class UserService(Resource):        
    # @api.marshal_list_with(signup)
    # @jwt.user_handler
    # def get(self):
    #     return User.query.get_by_name_and_password('cpi', 'unq').first()

    @api.doc(parser=user_parser)
    def post(self):
        args = user_parser.parse_args()
        user = User(username=args['username'], password=args['password'])
        # TODO mejorar la forma de generar el hash.
        #  sobreescribiendo el constructor falla al validar el password.
        #  no pude sobreescribir el save...
        user.generate_hashed_password()
        user.save()
        log.info("Crea nuevo Usuario: {'username':'%s'}" % user.username)
        return generate_token(user), 201
