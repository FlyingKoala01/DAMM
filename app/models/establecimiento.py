from ..extensions import db
from .distribuidor import Distribuidor

class Establecimiento(db.Model):
    ID = db.Column(db.CHAR, primary_key=True)
    nombre = db.Column(db.CHAR)
    coordenades = db.Column(db.CHAR, nullable=True)
    id_distribuidor = db.Column(db.CHAR, db.ForeignKey('distribuidor.ID'))
    average_grade = db.Column(db.Integer)
