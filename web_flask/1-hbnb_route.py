#!/usr/bin/python3
"""
'1-hbnb_route' is a Flask Web application starting script
"""
from flask import Flask


# Sets the current file as controller in an MVC Framework
web_app = Flask(__name__)


# Define a couple web app routes
# Home page
@web_app.route("/", strict_slashes=False)
def home():
    """Function to be called whenever the '/' route is utilized."""

    return "Hello HBNB!"


# Secondary path named 'hbnb'
@web_app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Function used whenever the '/hbnb' route is called upon."""

    return "HBNB"


if __name__ == "__main__":
    web_app.run()
