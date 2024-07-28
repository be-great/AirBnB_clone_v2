#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states', defaults={'id': None})
@app.route('/states/<id>')
def states(id):
    """displays a html page  with states"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html',
                           states=states,
                           id=id)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
