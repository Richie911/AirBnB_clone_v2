""" Starts flask application"""

from flask import Flask, render_template

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

@app.route('/number/<int:n>', strict_slashes=False)
def index(n):
    """displays n is a number"""
    if isinstance(n, int):
        return  (f"{n} is a number")

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """displays an HTML page"""
    return render_template('5-number.html', number=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_template(n):
    """displays an HTML page"""
    num= ""
    if num % 2 == 0:
        num = "even"
    else:
        num = "odd"
    return render_template('5-number.html', number=n, num = num)

if __name__ == "main":
    app.run(host="0.0.0.0", port=5000)