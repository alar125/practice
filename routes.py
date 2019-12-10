from flask import Blueprint, jsonify
from modules import db, Employee, Client

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
    return jsonify([(lambda client: client.json())(client) for client in Client.query.all()])

@api.route('/client/id/<int:client_id>')
def get_client(client_id):
    client = Client.query.get(client_id)
    return jsonify(client.json()) if client else ''

@api.route('/client/name/<string:client_name>')
def put_client(client_name):
    db.session.add(Client(name = client_name))
    db.session.commit()
    return 'done'

@api.route('/client/surname/<string:client_surname>')
def pt_client(client_surname):
    db.session.add(Client(surname = client_surname))
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
                  <a href = "./api/clients">Client</a>
              </body>
            </html>
           '''
