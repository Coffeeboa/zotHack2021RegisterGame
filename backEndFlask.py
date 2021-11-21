from flask import Flask
from flask import request
from flask_cors import CORS
import json

# cashier logic
EASY = 0
MEDIUM = 1
HARD = 2

import random


class Customer:
    def __init__(self, due: int or float, given: int or float):
        self._due = due
        self._given = given
        self._correct_change = round((self._given - self._due), 2)

    def due(self):
        return self._due

    def given(self):
        return self._given

    def correct_change(self):
        return self._correct_change


def _generate_amount_due(max_amount: int, decimals: int) -> float:
    '''Generate an amount due'''
    return round(random.random() * max_amount, decimals)


def _generate_amount_given(due: float, max_amount: int, decimals: int) -> int:
    add = round(random.random() * max_amount, decimals) + due
    return round(add, decimals)


class CustomerState:
    # TODO add levels and difficulty variability

    def __init__(self, line_length: int, difficulty: int):
        self._customer_line = []
        # TODO finish generating a list of customers
        if difficulty == EASY:
            self._customer_line = self._easy_customers(line_length)
            self._timer = 120


        elif difficulty == MEDIUM:
            self._customer_line = self._medium_customers(line_length)
            self._timer = 90

        elif difficulty == HARD:
            self._customer_line = self._hard_customers(line_length)
            self._timer = 60

    def _easy_customers(self, line_length: int) -> list[Customer]:
        line = []
        for x in range(line_length):
            due = _generate_amount_due(20, 0)
            given = _generate_amount_given(due, 10, 0)
            customer = Customer(due, given)
            line.append(customer)
        return line

    def _medium_customers(self, line_length: int) -> list[Customer]:
        line = []
        for x in range(line_length):
            due = _generate_amount_due(50, 2)
            given = _generate_amount_given(due, 25, 2)
            customer = Customer(due, given)
            line.append(customer)
        return line

    def _hard_customers(self, line_length: int) -> list[Customer]:
        line = []
        for x in range(line_length):
            due = _generate_amount_due(50, 2)
            given = _generate_amount_given(due, 50, 2)
            customer = Customer(due, given)
            line.append(customer)
        return line

    def customers_leave(self):
        new_customer_line = []
        for x in range(len(self._customer_line)):
            if self._customer_line[x].satisfaction() > 0:
                new_customer_line.append(self._customer_line[x])
        self._customer_line = new_customer_line

    def timer(self):
        return self._timer

    def line(self):
        return self._customer_line

    def remove_first_in_line(self):
        self._customer_line = self._customer_line[1:]


import time


app = Flask(__name__)
CORS(app)


difficulty = "Easy"
CurrentMoneyPicked = 0
# might be better to have a default line created here
line = CustomerState(5, 0)
startTime = 0
score = 0
amountDue = 0
cashGiven = 0



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
    global difficulty, amountDue, cashGiven
    global startTime, CurrentMoneyPicked, line, score
    totalTimePassed = time.time()-startTime

    if totalTimePassed > line.timer():
        return "Game ended, ran out of time"

    currentCustomer = line.line()[0]
    if currentCustomer.correct_change() == CurrentMoneyPicked:
        score += 100*(1+string_Difficult_to_int(difficulty))
    else:
        score -= 100 * (1 + string_Difficult_to_int(difficulty))


    line.remove_first_in_line()

    if (len(line.line()) == 0):

        difficulty = "Easy"
        CurrentMoneyPicked = 0
        # might be better to have a default line created here
        line = CustomerState(5, 0)
        startTime = 0

        amountDue = 0
        cashGiven = 0

        if score > 0:
            score = 0
            return "YOU WIN"
        score = 0
        return "YOU LOSE"

    # link with game here
    CurrentMoneyPicked = 0
    return str(score)


@app.route("/return_current_money_picked",methods=["POST"])
def return_current_money_picked():
    global CurrentMoneyPicked
    return str(CurrentMoneyPicked)


@app.route("/new_game",methods=["POST"])
def new_game():
    global difficulty, line, startTime
    startTime = time.time()
    line = CustomerState(5, string_Difficult_to_int(difficulty))
    print(str(line.line()[0].due()), str(line.line()[0].given()))
    returnTuple = [str(line.line()[0].due()),str(line.line()[0].given())]
    jsonObj = json.dumps(returnTuple)
    return jsonObj

@app.route("/return_amount_due_cash_given",methods=["POST"])
def return_amount_due_cash_given():
    returnTuple = [str(line.line()[0].due()), str(line.line()[0].given())]
    jsonObj = json.dumps(returnTuple)
    return jsonObj