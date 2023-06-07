from ..extensions import db

class Bar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    latitude = db.Column(db.Integer)
    longitude = db.Column(db.Integer)
    grade = db.Column(db.Integer)
    total_sales = db.Column(db.Integer)
    progress = db.Column(db.Integer)
    position = db.Column(db.Integer)
