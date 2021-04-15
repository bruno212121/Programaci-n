from flask_restful import Resource
from flask import request

BOLSONESPENDIENTES = {
    1: {'name': 'bolsonpendiente1'},
    2: {'name': 'bolsonpendiente2'},
    3: {'name': 'bolsonpendiente3'}
}

class BolsonPendiente(Resource):
    def get(self,id):
        if int(id) in BOLSONESPENDIENTES:
            return BOLSONESPENDIENTES[int(id)]
        return '', 404
    def delete(self,id):
        if int(id) in BOLSONESPENDIENTES:
            del BOLSONESPENDIENTES[int(id)]
            return '', 204
        return '', 404
    def put(self,id):
        if int(id) in BOLSONESPENDIENTES:
            bolson = BOLSONESPENDIENTES[int(id)]
            data = request.get_json()
            bolson.update(data)
            return bolson, 201
        return '', 404

class BolsonesPendientes(Resource):
    def get(self):
        return BOLSONESPENDIENTES
    def post(self):
        bolson = request.get_json()
        id = int(max(BOLSONESPENDIENTES.keys())) + 1
        BOLSONESPENDIENTES[id] = bolson
        return BOLSONESPENDIENTES[id], 201

