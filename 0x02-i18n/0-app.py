#!/usr/bin/python3
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    """
    Renders the home page.

    Returns:
        The rendered template for the home page.
    """

    return render_template('0-index.html')


if __name__ == '__main__':

    app.run(debug=True)
