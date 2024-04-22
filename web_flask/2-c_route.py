""" Starts flask application"""

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
    """displays c is ..."""
    return (f"C {text.replace('_', ' ')}")

if __name__ == "main":
    app.run(host="0.0.0.0", port=5000)