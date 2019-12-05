from flask import Blueprint, jsonify
from modules import db, Employee

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

@index.route('/')
@index.route('/index')
def get_index():
    return '''
           <html>
              <title>
                 Mega RESTful web service
              </title>
              <body>
                  <h3>API:</h3>
                  <a href = "./api/employees">Employee</a>
              </body>
            </html>
           '''
