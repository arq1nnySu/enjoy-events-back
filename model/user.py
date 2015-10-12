from api import db, log
from flask.ext.mongoalchemy import BaseQuery, document
from werkzeug.security import generate_password_hash, check_password_hash


class UserQuery(BaseQuery):
    def get_by_name(self, username):
        log.info("Busca un Usuario por nombre")
        return self.filter(self.type.username == username)


class User(db.Document):
    query_class = UserQuery
    username = db.StringField()
    password = db.StringField()

    def generate_hashed_password(self):
        self.password = generate_password_hash(self.password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
