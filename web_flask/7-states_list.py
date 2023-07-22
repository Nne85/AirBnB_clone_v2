#!/usr/bin/python3
"""
Starts a Flask web application that displays a list of States.
"""

from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """Closes the current SQLAlchemy Session."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a HTML page with the list of all State objects."""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
