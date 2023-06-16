from ..extensions import db

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80))
    sector = db.Column(db.String(80)) # Ej. Cervezas, Refrescos, etc.
    peso = db.Column(db.Float)
