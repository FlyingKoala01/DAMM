from ..extensions import db
from .distribuidor import Distribuidor

class Establecimiento(db.Model):
    id = db.Column(db.CHAR, primary_key=True)
    nombre = db.Column(db.CHAR)
    coordenades = db.Column(db.CHAR, nullable=True)
    id_distribuidor = db.Column(db.CHAR, db.ForeignKey('distribuidor.id'))
    average_grade = db.Column(db.Integer)
    nota_Ene= db.Column(db.Integer,nullable=True)
    nota_Feb= db.Column(db.Integer,nullable=True)
    nota_Mar= db.Column(db.Integer,nullable=True)
    nota_Abr= db.Column(db.Integer,nullable=True)
    nota_May= db.Column(db.Integer,nullable=True)
    nota_Jun= db.Column(db.Integer,nullable=True)
    nota_Jul= db.Column(db.Integer,nullable=True)
    nota_Ago= db.Column(db.Integer,nullable=True)
    nota_Sep= db.Column(db.Integer,nullable=True)
    nota_Oct= db.Column(db.Integer,nullable=True)
    nota_Nov= db.Column(db.Integer,nullable=True)
    nota_Dec= db.Column(db.Integer,nullable=True)
