from flask import Flask
from modules import db, Employee, Position, Client, Building
from routes import api, index

app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(index)
db.init_app(app)
with app.app_context():
    db.create_all()
    manager = Position(name = 'Manager')
    developer = Position(name = 'Developer')
    db.session.add(manager)
    db.session.add(developer)
    db.session.commit()
    db.session.add(Employee(name = 'Bob', position_id = manager.id))
    db.session.add(Employee(name = 'Rocky', position_id = developer.id))
    db.session.commit()

with app.app_context():
    db.create_all()
    ph = Building(name = 'Planet of Health')
    chamomile = Building(name = 'Chamomile')
    db.session.add(ph)
    db.session.add(chamomile)
    db.session.commit()
    db.session.add(Client(name = 'Mike', surname = 'Tompson', building_id = ph.id))
    db.session.commit()

if __name__ == '__main__':
    app.run()


