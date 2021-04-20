from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModel

BOLSONESPREVIOS = {
    1: {'name': 'bolsonprevio1'},
    2: {'name': 'bolsonprevio2'},
    3: {'name': 'bolsonesprevio3'}
}

class BolsonPrevio(Resource):
    def get(self,id):
        bolson = db.session.query(BolsonModel).get_or_404(id)
        return bolson.to_json()

class BolsonesPrevios(Resource):
    def get(self):
        bolsones = db.session.query(BolsonModel).all()
        return jsonify([bolson.to_json() for bolson in bolsones])
