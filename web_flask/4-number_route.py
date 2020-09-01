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


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """This function returns a string when accessing the /number/ route"""
    for chars in n:
        print(chars)
        if chars is not '.' and int(chars) >= 0 and int(chars) <= 9:
            pass
        else:
            return "Not a number!"
    return "{} is a number".format(n)
    #if isinstance(n, int):
    # if type(n) is int:
    #    return "{} is a number".format(n)
    #else:
    #    return str(type(n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
