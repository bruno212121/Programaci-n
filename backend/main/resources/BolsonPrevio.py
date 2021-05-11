from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModel
from datetime import timedelta, datetime

fecha = datetime.today() - timedelta(days=7)

class BolsonPrevio(Resource):

    def get(self,id):
        bolsonprevio = db.session.query(BolsonModel).get_or_404(id)
        if bolsonprevio.fecha <= fecha:
            return jsonify(bolsonprevio.to_json())
        else:
            return '', 404


class BolsonesPrevios(Resource):
    fecha = datetime.today() - timedelta(days=7)
    def get(self):
        page = 1
        per_page = 10

        bolsones = db.session.query(BolsonModel).filter(BolsonModel.fecha <= self.fecha)

        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key =="page":
                    page = int(value)
                if key =="per_page":
                    per_page = int(value)
        bolsones = bolsones.paginate(page, per_page, True, 30)

        return jsonify({
            'bolsonesprevios': [bolson.to_json() for bolson in bolsones.items],
            'total': bolsones.total,
            'pages': bolsones.pages,
            'page': page
        })
