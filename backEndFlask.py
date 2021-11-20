from flask import Flask
from flask import request
from flask_cors import CORS



app = Flask(__name__)
CORS(app)


diffculty = "NOT SET"

@app.route("/")
def hello_world():
    return "<p>Hello, test World!</p>"


@app.route("/update_difficulty",methods=["POST"])
def update_difficulty():
    print(request.form['difficulty'])
    return "200"