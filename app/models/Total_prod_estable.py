from ..extensions import db

class Total_Prod_estable(db.Model):
    id_establecimiento = db.Column(db.CHAR, db.ForeignKey('establecimiento.id'), primary_key=True)
    id_producto = db.Column(db.CHAR, db.ForeignKey('productos.id'), primary_key=True)
    total = db.Column(db.Integer)
