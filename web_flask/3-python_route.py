#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)
"""match both /name and /name/ and not only /name"""


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """display the text"""
    new_text = text.replace("_", " ")
    return f'C {text}'


@app.route('/python/', defaults={"text": "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def text_with_default(text):
    """display the text wiht default value"""
    new_text = text.replace("_", " ")
    return f'Python {text}'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)