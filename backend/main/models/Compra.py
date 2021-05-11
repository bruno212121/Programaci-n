from .. import db
import datetime as dt
from . import ClienteModel, BolsonModel

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fechacompra = db.Column(db.DateTime, nullable=False)
    retirado = db.Column(db.Boolean, nullable=False)
    bolson = db.relationship('Bolson', back_populates="compras", uselist=False, single_parent=True)
    bolsonId = db.Column(db.Integer, db.ForeignKey('bolson.id'), nullable=False)
    cliente = db.relationship('Cliente', back_populates="compras", uselist=False, single_parent=True)
    clienteId = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)

    def __repr__(self):
        return '<compra: %r %r >' % (self.fechacompra, self.retirado)
    #Convertir objeto en JSON
    def to_json(self):
        compra_json = {
            'id': self.id,
            'fechacompra': self.fechacompra.strftime('%Y-%m-%d'),
            'retirado': self.retirado,

        }
        return compra_json
    @staticmethod
    #Convertir JSON a objeto
    def from_json(compra_json):
        id = compra_json.get('id')
        retirado = compra_json.get('retirado')
        fechacompra = dt.datetime.strptime(compra_json.get('fechacompra'), '%Y-%m-%d')
        return Compra(id=id,
                    fechacompra=fechacompra,
                    retirado=retirado,
                    )
