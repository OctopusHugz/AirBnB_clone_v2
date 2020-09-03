#!/usr/bin/python3
"""This module starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_alive():
    """This function returns HTML when accessing the /hbnb route"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template('100-hbnb.html', states=states, places=places,
                           amenities=amenities)


@app.teardown_appcontext
def closing_time(self):
    """This function tears down and closes session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
