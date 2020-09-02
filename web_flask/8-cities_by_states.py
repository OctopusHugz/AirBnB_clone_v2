#!/usr/bin/python3
"""This module starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from os import getenv
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """This function returns HTML when accessing the /cities_by_states route"""
    states = storage.all(State).values()
    for state in states:
        if getenv('HBNB_TYPE_STORAGE') == 'db':
            cities = state.cities
        else:
            cities = storage.all(City).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def closing_time(self):
    """This function tears down and closes session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
