from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    location = db.Column(db.String(255), index=True)
    date = db.Column(db.Date, index=True)
    popularity = db.Column(db.Integer, index=True)
