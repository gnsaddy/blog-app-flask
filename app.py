from flask import Flask, render_template, json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite'


def load_data():
    with open("static/data.json") as f:
        return json.load(f)


data = load_data()


@app.route('/')
def index():

    return render_template("index.html")


@app.route('/post')
def post():

    return render_template("post.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
