from api import db
from user import User
from visibility import Visibility
from flask.ext.mongoalchemy import BaseQuery

class EventQuery(BaseQuery):

	def get_by_tag(self, tag):
		return self.filter(self.type.tag == tag)

class Event(db.Document):
	query_class = EventQuery
	tag = db.StringField()
	name = db.StringField()
	description = db.StringField()
	venue = db.StringField()
	time = db.StringField()
	date = db.StringField()
	image = db.StringField() 
	owner = db.DocumentField(User)
	visibility = db.DocumentField(Visibility)
