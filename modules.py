from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120))
    position_id = db.Column(db.Integer, ForeignKey('position.id'))
    position = relationship('Position')

    def json(self):
        return {"id": self.id, "name": self.name, "position": self.position.json()}

class Position(db.Model):
     __tablename__ = 'position'
     id = db.Column(db.Integer, primary_key = True)
     name = db.Column(db.String(120))

     def json(self):
         return {"id": self.id, "name": self.name}

##
class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120))
    surname = db.Column(db.String(120))
    building_id = db.Column(db.Integer, ForeignKey('building.id'))
    building = relationship('Building')

    def json(self):
        return {"id": self.id, "name": self.name, "surname": self.surname, "building": self.building.json()}

class Building(db.Model):
     __tablename__ = 'building'
     id = db.Column(db.Integer, primary_key = True)
     name = db.Column(db.String(120))

     def json(self):
         return {"id": self.id, "name": self.name}
