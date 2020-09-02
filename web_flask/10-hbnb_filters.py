#!/usr/bin/python3
"""This module starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """This function returns HTML when accessing the /states route"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def closing_time(self):
    """This function tears down and closes session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
