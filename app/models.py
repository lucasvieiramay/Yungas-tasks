import datetime

from app import db


class Task(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    description = db.Column(db.Text(), default='')
    deadline = db.Column(db.DateTime(), nullable=False)
    completed_at = db.Column(db.DateTime(), nullable=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return '<Task {}>'.format(self.title)
