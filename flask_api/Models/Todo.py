from flask_api import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)

    def __repr__(self):
        return f"Todo('{self.id}' , '{self.text}', '{self.complete}', {self.user_id})"
