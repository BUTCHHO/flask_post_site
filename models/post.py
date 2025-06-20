from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime
from .db import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(30), nullable = False)
    content = db.Column(db.Text(300), nullable = False)
    likes = db.Column(db.Integer, default=0)
    author_id = db.Column(db.String(), db.ForeignKey('account.id'))
    creation_date = db.Column(db.String(), default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    comments = db.relationship('Comment', backref='post', lazy=True)

    @hybrid_property
    def likes_count(self):
        return self.liked_by.count()

    @hybrid_property
    def comments_count(self):
        return len(self.comments)