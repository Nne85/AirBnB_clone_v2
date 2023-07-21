#!/usr/bin/python3
"""
This module defines a Flask web application with two routes.
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function handles the root URL and displays 'Hello HBNB!'.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function handles the '/hbnb' URL and displays 'HBNB'.
    """
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
