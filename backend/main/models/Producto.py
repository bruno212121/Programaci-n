from .. import db
#from . import ProveedorModel

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    usuario = db.relationship("usuario", back_populates="productos", uselist=False, single_parent=True)
    usuarioId = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    productobolsones = db.relationship("ProductoBolson", back_populates="producto", cascade="all, delete-orphan")

    def __repr__(self):
        return '<Producto: %r >' % (self.nombre)

    #Convertir objeto en JSON
    def to_json(self):
        producto_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'usuario': self.usuario.to_json(),

        }
        return producto_json
    @staticmethod
    #Convertir JSON a objeto
    def from_json(producto_json):
        id = producto_json.get('id')
        nombre = producto_json.get('nombre')
        usuarioId = producto_json.get('usuarioId')
        return Producto(id=id,
                    nombre=nombre,
                    usuarioId=usuarioId,
                    )
