#!/usr/bin/env python3
'''Get locale from request'''
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Define Config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('2-app.Config')


@babel.localeselector
def get_locale() -> str:
    '''Define get_locale'''
    return request.accept_languages.best_match(['en', 'fr'])


@app.route("/", methods=["GEt"], strict_slashes=False)
def hello_world() -> str:
    '''Define hello_world'''
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
