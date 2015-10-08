from api import db, log
from flask.ext.mongoalchemy import BaseQuery


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

