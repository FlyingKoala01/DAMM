from ..extensions import db

class Productos(db.Model):
    ID = db.Column(db.CHAR, primary_key=True)
    nombre = db.Column(db.CHAR)
    sector = db.Column(db.CHAR)
    peso = db.Column(db.Integer)
