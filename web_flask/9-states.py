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
def states_id(id):
    """This function returns HTML when accessing the /states/id route"""
    new_list = []
    id_list = []
    my_state = ""
    states = storage.all(State).values()
    for state in states:
        # if getenv('HBNB_TYPE_STORAGE') == 'db':
        #     cities = state.cities
        # else:
        #     cities = storage.all(City).values()
        if state.id == id:
            my_state = state
            new_list.append(state)
            id_list.append(state.id)
    return render_template('9-states.html', states=new_list, state=my_state,
                           id_list=id_list)


@app.teardown_appcontext
def closing_time(self):
    """This function tears down and closes session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
