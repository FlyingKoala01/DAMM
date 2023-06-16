from ..extensions import db
from .distribuidor import Distribuidor

class Establecimiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80))
    direccion = db.Column(db.String(80), nullable=True)
    id_distribuidor = db.Column(db.Integer, db.ForeignKey('distribuidor.id'))
    nota = db.Column(db.Integer)
