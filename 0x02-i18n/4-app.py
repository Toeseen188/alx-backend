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
    return render_template('4-index.html', home_title=_('home_title'),
                           home_header=_('home_header'))


class Config:
    """
    this is configuration class to translate lang
    """
    LANGUAGES = ["en", "fr"]

    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_locale():
    # Check if the 'locale' parameter is present in the request
    requested_locale = request.args.get('locale')

    if requested_locale and requested_locale in Config.LANGUAGES:
        return requested_locale  # Use the specified locale

    # Implement your logic to determine the user's preferred language here
    user_languages = request.accept_languages
    preferred_languages = Config.LANGUAGES

    for lang in preferred_languages:
        if lang in user_languages:
            return lang

    # If no preferred language is found, resort to the default behavior
    print("using the defaul lang")
    return app.config['BABEL_DEFAULT_LOCALE']


babel.init_app(app, locale_selector=get_locale)


if __name__ == '__main__':
    app.run(debug=True)
