#!/usr/bin/python3
"""This module starts a Flask web application"""
from web_flask import app


@app.route('/', strict_slashes=False)
def index():
    """This function returns a string when accessing the root index"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
