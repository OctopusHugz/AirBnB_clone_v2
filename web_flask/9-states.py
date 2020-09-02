#!/usr/bin/python3
"""This module starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from os import getenv
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """This function returns HTML when accessing the /states route"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    """This function returns HTML when accessing the /states/id route"""
    states = storage.all(State).values()
    for state in states:
        if getenv('HBNB_TYPE_STORAGE') == 'db':
            cities = state.cities
        else:
            cities = storage.all(City).values()
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def closing_time(self):
    """This function tears down and closes session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
