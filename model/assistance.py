from api import db
from model.user import User
from flask.ext.mongoalchemy import BaseQuery

class Requirement(db.Document):
	name = db.StringField()
	quantity = db.IntField()

	def __repr__(self):
		return "{0}:{1}".format(self.name, self.quantity)
	

class AssistanceQuery(BaseQuery):

	def get_requirements_by_event_tag(self, tag):
		assistances = self.filter(self.type.eventTag == tag).fields("requirements").all()
		requirements = map(lambda a: a.requirements, assistances)
		return reduce(list.__add__, requirements)
 
	def get_by_event(self, event):
		return self.filter(self.type.event == event).all()


	def get_by_user(self, user):
		return self.filter(self.type.user == user).all()

	def get_amount_by_event(self, event):
		return self.filter(self.type.event == event).count()


class AssistanceEvent(db.Document):
    tag = db.StringField()
    name = db.StringField()
    venue = db.StringField()
    time = db.StringField()
    date = db.StringField()
    image = db.StringField()

class Assistance(db.Document):
	query_class = AssistanceQuery
	eventTag = db.StringField()
	event = db.DocumentField(AssistanceEvent)
	user = db.DocumentField(User)
	requirements = db.ListField(db.DocumentField(Requirement))