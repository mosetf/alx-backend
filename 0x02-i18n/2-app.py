#!/usr/bin/env python3
"""
Basic Flask app module

This module contains a basic Flask app that uses Flask-Babel for internationalization (i18n).
It defines a Flask app, sets up Flask-Babel configuration, and includes routes for the home/index page.
"""

from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """
    Class representing a Flask Babel configuration.

    Attributes:
        LANGUAGES (list): List of supported languages.
        BABEL_DEFAULT_LOCALE (str): Default locale for translations.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for translations.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Function that retrieves the locale for a web page.

    Returns:
        str: The locale for the web page.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """
    Home/index page function
    
    Returns:
        str: The rendered template for the index page.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
