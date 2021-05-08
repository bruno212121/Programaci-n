from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProductoBolsonModel

class ProductoBolsones(Resource):
    def get(self):
        page = 1
        per_page = 10
        productobolsones = db.session.query(ProductoBolsonModel)
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'page':
                    page = int(value)
                elif key == 'per_page':
                    per_page = int(value)
        productobolsones = productobolsones.paginate(page, per_page, True, 30)

        return jsonify({
            'productobolsones': [productobolsones.to_json() for productobolsones in productobolsones.items],
            'total': productobolsones.total,
            'pages': productobolsones.pages,
            'page': page
        })


    def post(self):
        productobolsones = ProductoBolsonModel.from_json(request.get_json())
        db.session.add(productobolsones)
        db.session.commit()
        return productobolsones.to_json(), 201

class ProductoBolson(Resource):
    def get(self, id):
        productobolsones = db.session.query(ProductoBolsonModel).get_or_404(id)
        try:
            return productobolsones.to_json()
        except:
            return '', 404

    def delete(self, id):
        productobolsones = db.session.query(ProductoBolsonModel).get_or_404(id)
        try:
            db.session.delete(productobolsones)
            db.session.commit()
            return '', 204
        except:
            return '', 404

    def put(self, id):
        productobolsones = db.session.query(ProductoBolsonModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(productobolsones, key, value)
        try:
            db.session.add(productobolsones)
            db.session.commit()
            return productobolsones.to_json(), 201
        except:
            return '', 404