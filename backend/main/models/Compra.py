from .. import db
import datetime as dt

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fechacompra = db.Column(db.DateTime, nullable=False)
    retirado = db.Column(db.Boolean, nullable=False)

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
        fechacompra = dt.datetime.strptime(compra_json.get('fechacompra'), '%Y-%m-%d')
        retirado = compra_json.get('retirado')
        return Compra(id=id,
                    fechacompra=fechacompra,
                    retirado=retirado,
                    )
