from ..extensions import db

class Distribuidor(db.Model):
    ID = db.Column(db.CHAR, primary_key=True)
    nombre = db.Column(db.CHAR)
