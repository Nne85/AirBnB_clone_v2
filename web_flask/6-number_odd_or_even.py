#!/usr/bin/python3
"""
This module defines a Flask web application with seven routes.
"""

from flask import Flask, escape, render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    This function handles the '/number_template/<n>' URL and displays HTML page
    with the dynamic number inside an H1 tag in the BODY.
    """
    return render_template('6-number_template.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    This function handles the '/number_odd_or_even/<n>' & displays HTML page
    with the dynamic number and its odd/even status inside an H1 tag.
    """
    odd_or_even = "odd" if n % 2 else "even"
    return render_template('6-number_odd_or_even.html',
                           number=n, odd_even=odd_or_even)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
