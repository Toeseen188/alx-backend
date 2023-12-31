#!/usr/bin/env python3
"""Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _
from typing import List


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index() -> str:
    """
    index page
    """
    return render_template('3-index.html', home_title=_('home_title'),
                           home_header=_('home_header'))


class Config:
    """
    this is configuration class to translate lang
    """
    LANGUAGES: List[str] = ["en", "fr"]

    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app.config.from_object(Config)


def get_locale() -> str:
    """
    get the locale language using request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)

if __name__ == ('__main__'):
    app.run(debug=False)
