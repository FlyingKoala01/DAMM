from ..extensions import db

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_establecimiento = db.Column(db.Integer, db.ForeignKey('establecimiento.id'))
    id_producto = db.Column(db.String(10), db.ForeignKey('producto.id'))
    mes = db.Column(db.Date) # El dia del mes sera siempre 1.
    cantidad = db.Column(db.Integer)
