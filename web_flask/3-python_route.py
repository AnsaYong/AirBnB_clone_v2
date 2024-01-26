#!/usr/bin/python3
"""This module starts a Flask web application.
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)   # "/path" and "/path/" treated as same
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def process_c_text(text):
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/<text>", strict_slashes=False)
def process_python_text(text="is cool"):
    return "Python {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
def process_python_default():
    return process_python_text()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, use_reloader=False)
