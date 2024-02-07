#!/usr/bin/env python3
'''Mock logging in'''
from typing import Union
from flask import Flask, request, render_template, g
from flask_babel import Babel
from config import Config
from os import getenv

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Define Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('5-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    '''Define index'''
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    '''Define get_locale'''
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[dict, None]:
    '''Define get_user'''
    if request.args.get('login_as'):
        user = int(request.args.get('login_as'))
        if user in users:
            return users.get(user)
    else:
        return None


@app.before_request
def before_request():
    '''Define before_request'''
    g.user = get_user()


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)