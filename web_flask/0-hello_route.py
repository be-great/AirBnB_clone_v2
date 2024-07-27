#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)
"""match both /name and /name/ and not only /name"""


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display hello HBNB"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
