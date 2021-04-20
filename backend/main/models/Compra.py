from .. import db
import datetime as dt

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, primary_key=True)
    bolson_id = db.Column(db.Integer, primary_key=True)
    fechacompra = db.Column(db.DateTime, nullable=False)
    retirado = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<compra: %r %r %r %r >' % (self.cliente_id, self.bolson_id, self.fechacompra, self.retirado)
    #Convertir objeto en JSON
    def to_json(self):
        compra_json = {
            'id': self.id,
            'cliente_id': self.cliente_id,
            'bolson_id': self.bolson_id,
            'fechacompra': self.fechacompra.isoformat(),
            'retirado': self.retirado,

        }
        return compra_json
    @staticmethod
    #Convertir JSON a objeto
    def from_json(compra_json):
        id = compra_json.get('id')
        cliente_id = compra_json.get('cliente_id')
        bolson_id = compra_json.get('bolson_id')
        fechacompra = dt.datetime.strtime(compra_json.get('fecha'), '%y/%m/%d')
        retirado = compra_json.get('retirado')
        return Compra(id=id,
                    cliente_id=cliente_id,
                    bolson_id=bolson_id,
                    fechacompra=fechacompra,
                    retirado=retirado,
                    )
