#!/usr/bin/env python3
'''Display the current time'''
from datetime import datetime
from flask_babel import Babel, _, format_datetime
import flask_babel
from flask import Flask, render_template, request, g
import pytz
from typing import Union

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """Define Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('Config')


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[dict, None]:
    '''Define get_user'''
    try:
        login_as = request.args.get("login_as")
        user = users[int(login_as)]
    except Exception:
        user = None
    return user


@app.before_request
def before_request():
    '''Define before_request'''
    g.user = get_user()


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    '''Define hello_world'''
    timezone = get_timezone()
    tz = pytz.timezone(timezone)
    current_time = datetime.now(tz)
    current_time = format_datetime(datetime=current_time, locale=get_locale())
    return render_template("index.html", current_time=current_time)


@babel.localeselector
def get_locale() -> str:
    '''Define get_locale'''
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user:
        locale = g.user.get("locale")
        if locale and locale in app.config['LANGUAGES']:
            return locale
    locale = request.headers.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    '''Define get_timezone'''
    try:
        if request.args.get("timezone"):
            timezone = request.args.get("timezone")
            tz = pytz.timezone(timezone)
        elif g.user and g.user("timezone"):
            timezone = g.user.get("timezone")
            tz = pytz.timezone(timezone)
        else:
            timezone = app.config["BABEL_DEFAULT_TIMEZONE"]
            tz = pytz.timezone(timezone)
    except pytz.exceptions.UnknownTimeZoneError:
        timezone = "UTC"
    return timezone


if __name__ == "__main__":
    app.run()
