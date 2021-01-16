from flask import app
from flask_api import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

    def __repr__(self):
        return f"Todo('{self.public_id}' , '{self.name}', '{self.password}', {self.admin})"
