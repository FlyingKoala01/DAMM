from ..extensions import db

class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_establecimiento = db.Column(db.Integer, db.ForeignKey('establecimiento.id'))
    mes = db.Column(db.Date) # El dia del mes sera siempre 1.
    nota = db.Column(db.Integer)
    puntuacion_google = db.Column(db.Float)
