#!/usr/bin/python3
"""This module starts a Flask web application.
"""
from flask import Flask, render_template
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


@app.route("/python/", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def process_python_text(text):
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def process_integer(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, result='even')
    else:
        return render_template('6-number_odd_or_even.html', n=n, result='odd')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, use_reloader=False)
