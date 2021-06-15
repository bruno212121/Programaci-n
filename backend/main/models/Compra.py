from .. import db
import datetime as dt
#from . import UsuarioModel
from . import BolsonModel

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fechacompra = db.Column(db.DateTime, nullable=False)
    retirado = db.Column(db.Boolean, nullable=False)
    bolsonId = db.Column(db.Integer, db.ForeignKey('bolson.id'), nullable=False)
    bolson = db.relationship('Bolson', back_populates="compras", uselist=False, single_parent=True)
    usuarioId = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    usuario = db.relationship('Usuario', back_populates="compras")

    def __repr__(self):
        return '<compra: %r %r %r >' % (self.fechacompra, self.retirado, self.bolson.to_json())
    #Convertir objeto en JSON
    def to_json(self):
        compra_json = {
            'id': self.id,
            'fechacompra': self.fechacompra.strftime('%Y-%m-%d'),
            'retirado': self.retirado,
            'usuario': self.usuario.to_json(),
            'bolson': self.bolson.to_json()

        }
        return compra_json

    @staticmethod
    #Convertir JSON a objeto
    def from_json(compra_json):
        id = compra_json.get('id')
        retirado = compra_json.get('retirado')
        fechacompra = dt.datetime.strptime(compra_json.get('fechacompra'), '%Y-%m-%d')
        usuarioId = compra_json.get('usuarioId')
        bolsonId = compra_json.get('bolsonId')
        return Compra(id=id,
                    fechacompra=fechacompra,
                    retirado=retirado,
                    usuarioId=usuarioId,
                    bolsonId=bolsonId
                    )
