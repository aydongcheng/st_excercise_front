import json
from flask import Flask, jsonify
from flask import request
from flask_cors import *
import calendar


app = Flask(__name__)
CORS(app, resources=r'/*')


def brokerage():
    mainframe = {'price': 25, 'maxNum': 70}
    displayer = {'price': 30, 'maxNum': 80}
    peripheral = {'price': 45, 'maxNum': 90}
    data = request.get_data()
    dicts = json.loads(data)
    mNum = int(dicts['mainframe'])
    dNum = int(dicts['displayer'])
    pNum = int(dicts['peripheral'])
    index = int(dicts['index'])
    response = {}
    if mNum > 0 and dNum > 0 and pNum > 0:
        mNum = min(mainframe['maxNum'], mNum)
        dNum = min(displayer['maxNum'], dNum)
        pNum = min(peripheral['maxNum'], pNum)
        money = mNum * mainframe['price'] + dNum * displayer['price'] + pNum * peripheral['price']
        if money <= 1000:
            response['result'] = money * 0.1
        elif money <= 1800:
            response['result'] = money * 0.15
        else:
            response['result'] = money * 0.2
    else:
        response['result'] = 0
    response['index'] = index
    return json.dumps(response)


def is_triangle():
    data = request.get_data()
    dicts = json.loads(data)
    x = int(dicts['x'])
    y = int(dicts['y'])
    z = int(dicts['z'])
    index = int(dicts['index'])
    response = {}
    if x <= 0 | y <= 0 | z <= 0:
        response['result'] = "非三角形"
        response['index'] = index
        return json.dumps(response)
    if (x + y) <= z | (x + z) <= y | (y + z) <= x:
        response['result'] = "非三角形"
        response['index'] = index
        return json.dumps(response)
    if x == y == z:
        response['result'] = "等边三角形"
        response['index'] = index
        return json.dumps(response)
    if x == y | x == z | y == z:
        response['result'] = "等腰三角形"
        response['index'] = index
        return json.dumps(response)
    response['result'] = "一般三角形"
    response['index'] = index
    return json.dumps(response)


def isDigit(x):
    try:
        x = int(x)
        return True
    except ValueError:
        return False


def getDate():
    data = request.get_data()
    dicts = json.loads(data)
    response = {}
    index = int(dicts['index'])
    if isDigit(dicts['year']):
        year = int(dicts['year'])
    else:
        response['result'] = "error"
        response['index'] = index
        return json.dumps(response)
    if isDigit(dicts['month']):
        month = int(dicts['month'])
    else:
        response['result'] = "error"
        response['index'] = index
        return json.dumps(response)
    if isDigit(dicts['date']):
        date = int(dicts['date'])
    else:
        response['result'] = "error"
        response['index'] = index
        return json.dumps(response)
    if year < 1900 | year > 2050:
        response['result'] = "error"
        response['index'] = index
        return json.dumps(response)
    if month < 1 | month > 12:
        response['result'] = "error"
        response['index'] = index
        return json.dumps(response)
    if date < 1 | date > 31:
        response['result'] = "error"
        response['index'] = index
        return json.dumps(response)
    month = calendar.monthcalendar(year, month)
    month_len = 0
    for week in month:
        for day in week:
            if day != 0:
                month_len += 1
    if date > month_len:
        response['result'] = "error"
        response['index'] = index
        return json.dumps(response)
    for week in month:
        res = 0
        for day in week:
            res += 1
            if day == date:
                response['result'] = res
                break
    response['index'] = index
    return json.dumps(response)


@app.route('/commissionTest', methods=["POST"])
def commissionTest():
    return brokerage()


@app.route('/triAngelTest', methods=["POST"])
def triAngelTest():
    return is_triangle()


@app.route('/calendarTest', methods=["POST"])
def calendarTest():
    return getDate()


if __name__ == '__main__':
    app.run(debug=True)
