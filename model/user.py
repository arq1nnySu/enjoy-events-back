from api import db, log
from flask.ext.mongoalchemy import BaseQuery
from werkzeug.security import generate_password_hash, check_password_hash


class UserQuery(BaseQuery):
    def get_by_name_and_password(self, username, password):
        log.info("Busca un Usuario por nombre y password")
        return self.filter(self.type.username == username and self.type.password == password)

    def get_by_name(self, username):
        log.info("Busca un Usuario por nombre")
        return self.filter(self.type.username == username)


class User(db.Document):
    query_class = UserQuery
    username = db.StringField()
    password = db.StringField()

    def __init__(self, **kwargs):
        log.info('Creando un nuevo usuario con password = hash + salt')
        kwargs.update({'password': self.get_password(kwargs.pop('password'))})
        for k, v in kwargs.items():
            setattr(self, k, v)
        super(db.Document, self).__init__(kwargs)

    @staticmethod
    def get_password(password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
