from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProductoModel, ProveedorModel


class Producto(Resource):
    def get(self, id):
        try:
            producto = db.session.query(ProductoModel).get_or_404(id)
            return producto.to_json()
        except:
            return '', 404
    def put(self, id):
        producto = db.session.query(ProductoModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(producto, key, value)
        try:
            db.session.add(producto)
            db.session.commit()
            return producto.to_json(), 201
        except:
            return '', 404
    def delete(self, id):
        try:
            producto = db.session.query(ProductoModel).get_or_404(id)
            db.session.delete(producto)
            db.session.commit()
            return '', 204
        except:
            return '', 404

class Productos(Resource):
    def get(self):

        page = 1
        per_page = 10
        productos = db.session.query(ProductoModel)
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == "proveedorId":
                    productos = productos.filter(ProductoModel.proveedorId == value)
                elif key == 'page':
                    page = int(value)
                elif key == 'per_page':
                    per_page = int(value)

        productos = productos.paginate(page, per_page, True, 30)

        return jsonify({
            'productos': [producto.to_json() for producto in productos.items],
            'total': productos.total,
            'pages': productos.pages,
            'page': page
        })

    def post(self):
        try:
            producto = ProductoModel.from_json(request.get_json())
            db.session.add(producto)
            db.session.commit()
            return producto.to_json(), 201
        except:
            return '', 404
