from api import db, log
from user import User
from visibility import Visibility
from assistance import Assistance, Requirement
from flask.ext.mongoalchemy import BaseQuery
from itertools import groupby
from operator import itemgetter

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
    requirement = db.ListField(db.DocumentField(Requirement))
    capacity = db.IntField()

    def hasAccess(self, user):
        log.info("Verificar acceso del Usuario: {'username':'%s'} al Evento con: {'tag':'%s'}" % (user.username, self.tag))
        return self.visibility.isPublic() or self.owner == user or user in self.gests
    
    def availability(self):
        log.info("Calcular la disponibilidad del Evento con: {'tag':'%s'}" % self.tag)
        return self.capicity - Assistance.query.get_amount_by_event(self.tag)

    def lackRequirements(self):
        log.info("Suma todos los requisitos que los usuarios se comprometieron a llevar al evento.")
        lack = [] 
        requirements = Assistance.query.get_requirements_by_event_tag(self.tag)
        keyfunc = lambda r: r.name

        for req in requirements : req.quantity = -req.quantity
        requirements += self.requirement
        requirements.sort(key=keyfunc)

        for name, reqs in groupby(requirements,key=keyfunc):
            lack.append(Requirement(name=name, quantity= sum(req.quantity for req in reqs)))
        return lack
