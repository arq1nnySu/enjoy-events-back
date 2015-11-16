from flask.ext.restplus import Resource
from api import api, signup, user_parser, log, UsersDC, app, mailService
from services.jwtService import jwt, generate_token, login_required, currentUser
from model.user import User

us = api.namespace('user', description='Servicios para usuario')

@us.route('')
class UserService(Resource):        
    @api.marshal_with(signup)
    @login_required()
    def get(self):
        return currentUser()

    @api.doc(parser=user_parser)
    @login_required()
    def put(self):
        args = user_parser.parse_args()
        user = currentUser()
        user.email = args.email
        user.firstName = args.firstName
        user.lastName = args.lastName
        user.phone = args.phone
        user.save()
        return 201

    @api.doc(parser=user_parser)
    def post(self):
        args = user_parser.parse_args()
        user = User(username=args.username, 
                    password=args.password,
                    email=args.email,
                    firstName = args.firstName, 
                    lastName=args.lastName,
                    phone=args.phone)
        # TODO mejorar la forma de generar el hash.
        #  sobreescribiendo el constructor falla al validar el password.
        #  no pude sobreescribir el save...
        user.generate_hashed_password()
        user.save()
        mailService.createUser(user)
        log.info("Crea nuevo Usuario: {'username':'%s'}" % user.username)
        return generate_token(user), 201


uss = api.namespace('users', description='Servicios para usuario')

@uss.route('')
class UsersService(Resource):
    @api.marshal_list_with(UsersDC)
    @login_required()
    def get(self):
        return User.query.filter(User.username != currentUser().username).all()


