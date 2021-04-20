from .. import db

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    proveedor_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return '<Professor: %r %r >' % (self.proveedor_id, self.nombre)
    #Convertir objeto en JSON
    def to_json(self):
        producto_json = {
            'id': self.id,
            'proveedor_id': self.proveedor_id,
            'nombre': str(self.nombre),

        }
        return producto_json
    @staticmethod
    #Convertir JSON a objeto
    def from_json(producto_json):
        id = producto_json.get('id')
        proveedor_id = producto_json.get('proveedor_id')
        nombre = producto_json.get('nombre')
        return Producto(id=id,
                    proveedor_id=proveedor_id,
                    nombre=nombre,
                    )
