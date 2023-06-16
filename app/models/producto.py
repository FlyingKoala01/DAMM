from ..extensions import db

class Producto(db.Model):
    id = db.Column(db.String(10), primary_key=True)
    nombre = db.Column(db.String(80))
    sector = db.Column(db.String(80)) # Ej. Cervezas, Refrescos, etc.
    # El peso indica la rellevancia de un producto. Un numero de 0 a 1.
    # Por ejemplo, un pack de 6 cervezas tiene un peso menor que un pack de 12.
    # Actualmente se usan valores aleatorios, pero se pueden cambiar en
    # cualquier momento.
    peso = db.Column(db.Float)
