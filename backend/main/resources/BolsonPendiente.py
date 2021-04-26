from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModel
from datetime import datetime

BOLSONESPENDIENTES = {
    1: {'name': 'bolsonpendiente1'},
    2: {'name': 'bolsonpendiente2'},
    3: {'name': 'bolsonpendiente3'}
}

class BolsonPendiente(Resource):
    def get(self,id):
        bolsonpendiente = db.session.query(BolsonModel).get_or_404(id)
        return bolsonpendiente.to_json()
    def delete(self,id):
        bolsonpendiente = db.session.query(BolsonModel).get_or_404(id)
        db.session.delete(bolsonpendiente)
        db.session.commit()
        return '', 204
    def put(self,id):
        bolsonpendiente = db.session.query(BolsonModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(bolsonpendiente, key, value)
        db.session.add(bolsonpendiente)
        db.session.commit()
        return bolsonpendiente.to_json(), 201

class BolsonesPendientes(Resource):
    def get(self):
        bolsones = db.session.query(BolsonModel).all()
        return jsonify([bolson.to_json() for bolson in bolsones])
    def post(self):
        bolson = BolsonModel.from_json(request.get_json())
        db.session.add(bolson)
        db.session.commit()
        return bolson.to_json(), 201