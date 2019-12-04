from flask import Blueprint, jsonify
from modules import Men, db, Client

api = Blueprint('api', __name__, url_prefix='/api')

#class - Men
@api.route('/mens')
def get_mens():
    return jsonify([(lambda men: men.json())(men) for men in Men.query.all()])

@api.route('/men/id/<int:men_id>')
def get_men(men_id):
    men = Men.query.get(men_id)
    return jsonify(men.json()) if men else ''

@api.route('/men/name/<string:men_name>')
def put_men(men_name):
    db.session.add(Men(name = men_name))
    db.session.commit()
    return 'done'

#class - Client
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
