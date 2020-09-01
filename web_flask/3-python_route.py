#!/usr/bin/python3
"""This module starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """This function returns a string when accessing the root index"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This function returns a string when accessing the /hbnb route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """This function returns a string when accessing the /c/ route"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """This function returns a string when accessing the /python/ route"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
