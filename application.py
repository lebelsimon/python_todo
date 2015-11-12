#! /usr/bin/env python3

from flask import Flask, render_template
app = Flask(__name__)
app.debug = True

global dico
dico = {"michel":["manger","bouger",".com"],
        "Batman":["say IM THE BATMAN","then wait"],
        "Pikachu":["pika","pika pika","pika","pika"],
        "Monsieur oui":["Dire oui","Et encore oui"],
        None:["L'anonyme est un glandeur"]
}

@app.route('/')
def home():
    return render_template(
        "home.html")

@app.route('/user/')
@app.route('/user/<name>')
def user(name=None):
    global dico
    # todo=["rien", "pas grand chose", "sieste"]
    if name not in dico.keys():
        dico[name]=['new user without tasks']
    return render_template(
        "user.html",
        name=name,
        todo=dico[name])

if __name__ == '__main__':
    app.run(host="0.0.0.0")
