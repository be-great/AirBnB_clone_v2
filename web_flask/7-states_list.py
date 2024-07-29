#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """display HBNB"""
    state = storage.all(State)
    return render_template("7-states_list.html", states=state)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
