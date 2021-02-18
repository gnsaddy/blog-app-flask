from flask import Flask, render_template, json

app = Flask(__name__)


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
