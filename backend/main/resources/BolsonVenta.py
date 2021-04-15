from flask_restful import Resource
from flask import request

BOLSONESVENTA = {
    1: {'name': 'bolsónventa1'},
    2: {'name': 'bolsónventa2'},
    3: {'name': 'bolsónventa3'},
    4: {'name': 'bolsonventa4'}
}

class BolsonesVenta(Resource):
    def get(self):
        return BOLSONESVENTA

class BolsonVenta(Resource):
    def get(self, id):
        if int(id) in BOLSONESVENTA:
            return BOLSONESVENTA[int(id)]
        return '', 404
