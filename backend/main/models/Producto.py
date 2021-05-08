from .. import db
from main.models import ProveedorModel

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    proveedor = db.relationship("Proveedor", back_populates="productos", uselist=False, single_parent=True)
    proveedorid = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)
    productobolsones = db.relationship("ProductoBolson", back_populates="producto", cascade="all, delete-orphan")

    def __repr__(self):
        return '<Producto: %r  %r %r >' % (self.nombre, self.proveedorid, self.id)

    #Convertir objeto en JSON
    def to_json(self):
        producto_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'proveedorid': self.proveedorid,

        }
        return producto_json
    @staticmethod
    #Convertir JSON a objeto
    def from_json(producto_json):
        id = producto_json.get('id')
        nombre = producto_json.get('nombre')
        proveedorid = producto_json.get('proveedorid')
        return Producto(id=id,
                    nombre=nombre,
                    proveedorid=proveedorid,
                    )
