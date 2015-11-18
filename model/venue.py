from api import db, log
from flask.ext.mongoalchemy import BaseQuery


class VenueQuery(BaseQuery):
    def get_by_name(self, name):
        return self.filter(self.type.name == name).first_or_404()

class Venue(db.Document):
    query_class = VenueQuery
    name = db.StringField()
    street = db.StringField()
    city = db.StringField()
    country = db.StringField()