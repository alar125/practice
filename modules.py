from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Men(db.Model):
    __tablename__ = 'mens'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120))

    def json(self):
        return {"id": self.id, "name": self.name}

class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120))
    surname = db.Column(db.String(120))

    def json(self):
        return {"id": self.id, "name": self.name, "surname": self.surname}
