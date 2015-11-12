#! /usr/bin/env python3
from db import *

from flask import Flask, render_template
app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return render_template(
        "home.html")

@app.route('/user/')
@app.route('/user/<name>')
def user(name = None):
    data = DB()
    todol=[]
    # todo=["rien", "pas grand chose", "sieste"]
    for elem in data.get(name):
        todol.append(elem[1])
    return render_template(
        "user.html",
        name=name,
        todo=todol)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
