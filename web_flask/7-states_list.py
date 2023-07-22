#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(error):
    """Closes the database again at the end of the request."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display HTML page with the list of all State objects sorted by name."""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
