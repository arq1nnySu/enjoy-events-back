from api import db
from model.user import User
from flask.ext.mongoalchemy import BaseQuery

class AssistanceQuery(BaseQuery):

	def get_requirements_by_event(self, event):
		assistances = self.filter(self.type.event == event).fields("requirement").all()
		requirements = map(lambda a: a.requirement, assistances)
		return reduce(list.__add__, requirements)
 
	def get_by_event(self, event):
		return self.filter(self.type.event == event).all()

	def get_amount_by_event(self, event):
		return self.filter(self.type.event == event).count()

class Assistance(db.Document):
	query_class = AssistanceQuery
	event = db.StringField()
	user = db.DocumentField(User)
	requirement = db.ListField(db.TupleField(db.StringField(), db.IntField()))