from flask_restful import Resource
from flask import request

BOLSONES = {
    1: {'name': 'bolson1'},
    2: {'name': 'bolson2'},
    3: {'name': 'bolson3'}
}

class Bolson(Resource):
    def get(self, id):
        if int(id) in BOLSONES:
            return BOLSONES[int(id)]
        return '', 404

class Bolsones(Resource):
    def get(self):
        return BOLSONES
