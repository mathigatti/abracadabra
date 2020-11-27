from flask import Flask
from flask import render_template
from flask import request
import os

app = Flask(__name__)

def execute_task():
	print("abracadabra")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/command')
def command():
    score = request.args.get('score')
    if float(score) > 0.8:
	    execute_task()
    return "ok"