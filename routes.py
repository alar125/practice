from flask import Blueprint, jsonify
from modules import db, Employee, Client, Building

api = Blueprint('api', __name__, url_prefix='/api')
index = Blueprint('index', __name__, url_prefix='/')

@api.route('/employees')
def get_employees():
    return jsonify([(lambda employee: employee.json())(employee) for employee in Employee.query.all()])

@api.route('/employee/id/<int:employee_id>')
def get_employee(employee_id):
    employee = Employee.query.get(employee_id)
    return jsonify(employee.json()) if employee else ''

@api.route('/employee/name/<string:employee_name>')
def put_employee(employee_name):
    db.session.add(Employee(name = employee_name))
    db.session.commit()
    return 'done'

##
@api.route('/clients')
def get_clients():
    return jsonify([(lambda client: client.json())(client) for client in Client.query.all()])\

@api.route('/buildings')
def get_buildings():
    return jsonify([(lambda building: building.json())(building) for building in Building.query.all()])

@api.route('/building/id/<int:building_id>')
def get_building(building_id):
    building = Building.query.get(building_id)
    return jsonify(building.json()) if building else ''

@api.route('/building/name/<string:building_name>')
def put_building(building_name):
    db.session.add(Building(name = building_name))
    db.session.commit()
    return 'done'

@api.route('/client/id/<int:client_id>')
def get_client(client_id):
    client = Client.query.get(client_id)
    return jsonify(client.json()) if client else ''

@api.route('/client/name/<string:client_name>/surname/<string:client_surname>/building/<string:building_name>')
def put_client(client_name,client_surname,building_name):
    building = Building.query.filter_by(name=building_name).all()[0]
    db.session.add(Client(name = client_name,surname = client_surname, building_id = building.id))
    db.session.commit()
    return 'done'

@index.route('/')
@index.route('/index')
def get_index():
    return '''
           <html>
              <title>
                 Pharm Web Service
              </title>
              <body>
                  <h3>MENU:</h3>
                  <a href = "./api/clients">Client</a><br>
                  <a href = "./api/buildings">Building</a>
              </body>
            </html>
           '''
