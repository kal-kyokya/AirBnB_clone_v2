#!/usr/bin/python3
"""
'2-c_route' is a Flask web application starting module
"""
# Import the Flask class from the flask module
from flask import Flask


# Specify the current file as the web app controller
app = Flask(__name__)


# Define route handling mechanisms
@app.route("/", strict_slashes=False)
def home():
    """Function handling '/' route requests.

    Return:
        A string text.
    """
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Function called when the '/hbnb' route is taken.

    Return:
        A string text.
    """
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Function used when the '/c/' routes is used with a URL input text.

    Arg:
        text: URL Input text to be used.

    Return:
        A string text.
    """
    return ("C " + text.replace('_', ' '))


if __name__ == "__main__":
    app.run()
