#!/usr/bin/python3
"""This module starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list(states):
    """This function returns HTML when accessing the /states_list route"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown():
    """This function tears down and closes session"""
    storage.close()
    

if __name__ == "__main__":
    app.run(host="0.0.0.0")
