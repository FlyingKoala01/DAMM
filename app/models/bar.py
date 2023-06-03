from ..extensions import db

class Bar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bar_name = db.Column(db.Text)
    latitude = db.Column(db.Integer)
    longitude = db.Column(db.Integer)
    ranking = db.Column(db.Integer)
    total_sales = db.Column(db.Integer)
    progress = db.Column(db.Integer)
