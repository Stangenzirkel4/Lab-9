from collections import namedtuple
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

Message = namedtuple('Message', 'text tag')
messages = []

def add_something():
    return 0

@app.route("/", methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route("/main", methods=['GET'])
def main():
    return render_template('main.html', messages=messages)


@app.route("/add_message", methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']
    messages.append(Message(text, tag))
    return render_template('main.html', messages=messages)

#commit
