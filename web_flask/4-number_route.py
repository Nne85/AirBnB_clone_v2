#!/usr/bin/python3
"""
This module defines a Flask web application with five routes.
"""

from flask import Flask, escape

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


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    This function handles the '/c/<text>' URL and displays 'C ',
    followed by the value of the text variable (replace underscores
    with spaces).
    """
    return 'C ' + escape(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    This function handles the '/python/' and '/python/<text>' URLs and
    displays 'Python ', followed by the value of the text variable
    (replace underscores with spaces). If no text is provided, the
    default value 'is cool' is used.
    """
    return 'Python ' + escape(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    This function handles the '/number/<n>' URL and displays 'n is a number'
    only if n is an integer.
    """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
