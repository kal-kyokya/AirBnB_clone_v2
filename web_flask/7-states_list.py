#!/usr/bin/python3
"""
'7-states_list' is a script that starts a Flask Web Application
"""
from models import *
from models import storage
from flask import Flask, render_template


# Sets this script to be the controller in this Framework
app = Flask(__name__)


# Definitions for associated routes
@app.route("/states_list", strict_slashes=False)
def states_list():
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
