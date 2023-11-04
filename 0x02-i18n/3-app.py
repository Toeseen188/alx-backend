#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index():
    """
    index page
    """
    return render_template('3-index.html', home_title=_('home_title'),
                           home_header=_('home_header'))


class Config:
    """
    this is configuration class to translate lang
    """
    LANGUAGES = ["en", "fr"]

    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel.init_app(app)


@babel.localeselector
def get_locale():
    """
    get the locale language using request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == ('__main__'):
    app.run(debug=False)
