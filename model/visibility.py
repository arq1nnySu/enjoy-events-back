from api import db
from flask.ext.mongoalchemy import BaseQuery


class VisibilityQuery(BaseQuery):
	def public(self):
		return self.get('Public')

	def private(self):
		return self.get('Private')

	def get(self, name):
		return self.filter(self.type.name == name).first()


class Visibility(db.Document):
	query_class = VisibilityQuery
	name  = db.StringField()

	def isPublic(self):
		return self.name == 'Public'

