from ..extensions import db

class Total_Prod_estable(db.Model):
    id_establecimiento = db.Column(db.CHAR, db.ForeignKey('Establecimiento.ID'), primary_key=True)
    id_producto = db.Column(db.CHAR, db.ForeignKey('Productos.ID'), primary_key=True)
    total = db.Column(db.Integer)
