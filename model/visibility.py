from api import db
from flask.ext.mongoalchemy import BaseQuery


class VisibilityQuery(BaseQuery):
	def public(self):
		return self.filter(self.type.name == 'Public').first()

	def private(self):
		return self.filter(self.type.name == 'Private').first()


class Visibility(db.Document):
	query_class = VisibilityQuery
	name  = db.StringField()

