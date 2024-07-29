#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)
"""match both /name and /name/ and not only /name"""


@app.route('/states_list', strict_slashes=False)
def list_states():
    """display HBNB"""
    sorted_state = sorted(list(storage.all("State").values()),
                          key=lambda x: x.name)
    return render_template("7-states_list.html", states=sorted_state)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
