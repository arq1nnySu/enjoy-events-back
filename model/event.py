from api import db, log
from user import User
from visibility import Visibility
from flask.ext.mongoalchemy import BaseQuery


class EventQuery(BaseQuery):
    def get_by_tag(self, tag):
        log.info("Busca un Evento con: {'tag':%s}" % tag)
        return self.filter(self.type.tag == tag).first()


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
    gests = db.ListField(db.DocumentField(User))

    def hasAccess(self, user):
        log.info(
            "Verificar acceso del Usuario: {'username':'%s'} al Evento con: {'tag':'%s'}" % (user.username, self.tag))
        return self.visibility.isPublic() or self.owner == user or user in self.gests
