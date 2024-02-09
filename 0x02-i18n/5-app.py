#!/usr/bin/env python3
'''Mock logging in'''
from typing import Union
from flask import Flask, render_template, request, g
from flask_babel import Babel
from os import getenv

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Define Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('5-app.Config')


@app.before_request
def before_request():
    '''Define before_request'''
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    '''Define get_locale'''
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    '''Define index'''
    return render_template('5-index.html')


def get_user() -> Union[dict, None]:
    '''Define get_user'''
    try:
        login_as = request.args.get('login_as', None)
        user = users[int(login_as)]
    except Exception:
        user = None


if __name__ == "__main__":
    app.run()
