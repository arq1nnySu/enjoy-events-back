from api import db


class Event(db.Document):
	tag = db.StringField()
	name = db.StringField()
	description = db.StringField()
	venue = db.StringField()
	time = db.StringField()
	date = db.StringField()
	image = db.StringField()


