from ..extensions import db
from .distribuidor import Distribuidor

class Establecimiento(db.Model):
    id = db.Column(db.CHAR, primary_key=True)
    nombre = db.Column(db.CHAR)
    coordenades = db.Column(db.CHAR, nullable=True)
    id_distribuidor = db.Column(db.CHAR, db.ForeignKey('distribuidor.id'))
    average_grade = db.Column(db.Integer)
