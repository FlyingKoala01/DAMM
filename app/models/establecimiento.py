from ..extensions import db
from sqlalchemy import func
from .venta import Venta

class Establecimiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80))
    direccion = db.Column(db.String(80), nullable=True)
    id_distribuidor = db.Column(db.Integer, db.ForeignKey('distribuidor.id'))
    nota = db.Column(db.Float, nullable=True)
    nota_anterior = db.Column(db.Float, nullable=True)

    def total_sales(self):
        total = db.session.query(func.sum(Venta.cantidad)).filter(Venta.id_establecimiento == self.id).scalar()
        return total or 0

    def get_previous_position(self):
        position = db.session.query(func.count('*')).filter(Establecimiento.nota_anterior > self.nota_anterior).scalar()
        return position+1
    
    def get_current_position(self):
        position = db.session.query(func.count('*')).filter(Establecimiento.nota > self.nota).scalar()
        return position+1
