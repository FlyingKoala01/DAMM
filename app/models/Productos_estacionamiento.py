from ..extensions import db

class Prod_esta(db.Model):
    id_establecimiento = db.Column(db.CHAR, db.ForeignKey('establecimiento.ID'), primary_key=True)
    id_producto = db.Column(db.CHAR, db.ForeignKey('productos.ID'), primary_key=True)
    año_mes = db.Column(db.CHAR, primary_key=True)
    cantidad = db.Column(db.Integer)
