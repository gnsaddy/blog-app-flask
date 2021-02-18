from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=True)
    author = db.Column(db.String(50), nullable=False, default="N/A")
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __repr__(self):
        return 'Blog Post ' + str(self.id)


