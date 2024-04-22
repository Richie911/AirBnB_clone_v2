#!/usr/bin/python3
"""script that runs flask application"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """displays "Hello HBNB!"""
    return ("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def index():
    """displays "HBNB"""
    return ("HBNB")

@app.route('/c/<text>', strict_slashes=False)
def index(text):
    """displays C is ..."""
    return (f"C {text.replace('_', ' ')}")

@app.route('/python/<text>', strict_slashes=False)
def index(text="is cool"):
    """displays Python is ..."""
    return (f"Python {text.replace('_', ' ')}")

@app.route('/number/<n>', strict_slashes=False)
def index(n):
    """displays n is a number"""
    if isinstance(n, int):
        return  (f"{n} is a number")

if __name__ == "main":
    app.run(host="0.0.0.0", port=5000)