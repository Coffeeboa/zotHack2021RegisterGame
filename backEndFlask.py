from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


difficulty = "NOT SET"
CurrentMoneyPicked = 0


def string_Difficult_to_int(str):
    # currently impossible is the same as easy
    mapping = {"Easy":0,"Medium":1,"Hard":2,"Impossible":0}
    return mapping.get(str)


@app.route("/")
def hello_world():
    return "<p>Hello, test World!</p>"


@app.route("/update_difficulty",methods=["POST"])
def update_difficulty():
    global difficulty
    difficulty = string_Difficult_to_int(request.form['difficulty'])
    print(request.form['difficulty'])
    return "200"


@app.route("/picked_more_money",methods=["POST"])
def picked_more_money():
    global CurrentMoneyPicked
    print('picked more money')
    CurrentMoneyPicked += float(request.form['dollarAmount'])
    CurrentMoneyPicked = round(CurrentMoneyPicked, 2)

    print(CurrentMoneyPicked)
    return "200"


@app.route("/submit_and_clear",methods=["POST"])
def submit_and_clear():
    global CurrentMoneyPicked
    # link with game here
    CurrentMoneyPicked = 0
    return "200"


@app.route("/return_current_money_picked",methods=["POST"])
def return_current_money_picked():
    global CurrentMoneyPicked
    return str(CurrentMoneyPicked)



