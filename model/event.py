from api import db


class Event(db.Document):
    def __init__(self, kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


