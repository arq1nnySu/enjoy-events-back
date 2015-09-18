from api import db
from flask.ext.mongoalchemy import BaseQuery


class UserQuery(BaseQuery):

    def get_by_name_and_password(self, username, password):
        return self.filter(self.type.username == username and self.type.password == password)


class User(db.Document):
    query_class = UserQuery
    username = db.StringField()
    password = db.StringField()

