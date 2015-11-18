from api import db, log
from flask.ext.mongoalchemy import BaseQuery


class VisibilityQuery(BaseQuery):
    def public(self):
        return self.get('Public')

    def private(self):
        return self.get('Private')

    def get(self, name):
        log.info("Busca la Visibilidad: %s de un Evento." % name)
        return self.filter(self.type.name == name).first_or_404()


class Visibility(db.Document):
    query_class = VisibilityQuery
    name = db.StringField()

    def isPublic(self):
        return self.name == 'Public'

    def __repr__(self):
        return self.name
