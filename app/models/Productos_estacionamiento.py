from ..extensions import db

class Prod_esta(db.Model):
    id_establecimiento = db.Column(db.CHAR, db.ForeignKey('establecimiento.id'), primary_key=True)
    id_producto = db.Column(db.CHAR, db.ForeignKey('productos.id'), primary_key=True)
    year_month = db.Column(db.CHAR, primary_key=True)
    cantidad = db.Column(db.Integer)
