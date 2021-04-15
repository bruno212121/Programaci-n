from flask_restful import Resource
from flask import request

BOLSONESPREVIOS = {
    1: {'name': 'bolsonprevio1'},
    2: {'name': 'bolsonprevio2'},
    3: {'name': 'bolsonesprevio3'}
}

class BolsonPrevio(Resource):
    def get(self,id):
        if int(id) in BOLSONESPREVIOS:
            return BOLSONESPREVIOS[int(id)]
        return '', 404

class BolsonesPrevios(Resource):
    def get(self):
        return BOLSONESPREVIOS
