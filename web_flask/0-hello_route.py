#!/usr/bin/python3
"""
'0-hello_route' is a Flask web application starting script
"""
from flask import Flask


# Turn the current file into a Framework controller
app = Flask(__name__)


# Define actions ensuing access to the 'home page'
@app.route("/", strict_slashes=False)
def home():
    """Function to be called when the '/' route is taken."""

    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
