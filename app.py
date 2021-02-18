from flask import Flask, render_template, json, request
from models import BlogPost, db

app = Flask(__name__)

@app.route('/')
def index():

    return render_template("index.html")


@app.route('/post', methods=["GET", "POST"])
def post():
    if request.method == "POST":
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']


    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)
