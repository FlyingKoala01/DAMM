from ..extensions import db

class Bar(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.Integer)
    name = db.Column(db.String(80))
    latitude = db.Column(db.Integer)
    longitude = db.Column(db.Integer)
    grade = db.Column(db.Integer)
    total_sales = db.Column(db.Integer)
    progress = db.Column(db.Integer)