from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModel

BOLSONESVENTA = {
    1: {'name': 'bolsónventa1'},
    2: {'name': 'bolsónventa2'},
    3: {'name': 'bolsónventa3'},
    4: {'name': 'bolsonventa4'}
}

class BolsonesVenta(Resource):
    def get(self):
        bolsones = db.session.query(BolsonModel).all()
        return jsonify([bolson.to_json() for bolson in bolsones])

class BolsonVenta(Resource):
    def get(self, id):
        bolson = db.session.query(BolsonModel).get_or_404(id)
        return bolson.to_json()
