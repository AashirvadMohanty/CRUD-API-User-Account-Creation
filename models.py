from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    first_name = db.Column(db.String(1000))
    last_name = db.Column(db.String(1000))
    password = db.Column(db.String(100))