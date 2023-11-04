#!/usr/bin/env python3
"""
Flask app
"""
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index():
    """
    index page
    """
    return render_template('0-index.html')


class Config:
    """ this is configuration class to translate lang
    """
    LANGUAGES = ["en", "fr"]

    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel.init_app(app)

if __name__ == ('__main__'):
    app.run(debug=False)
