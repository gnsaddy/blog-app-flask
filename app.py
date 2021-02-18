from flask import Flask, render_template, json, request, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=True)
    author = db.Column(db.String(50), nullable=False, default="N/A")
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __repr__(self):
        return 'Blog Post ' + str(self.id)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/post', methods=["GET", "POST"])
def post():
    if request.method == "POST":
        post_title = request.form['title']
        post_content = request.form['post']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect("/post")
    else:
        data = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)
