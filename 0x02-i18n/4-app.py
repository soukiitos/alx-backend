#!/usr/bin/env python3
'''Force locale with URL parameter'''
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Define Config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('4-app.Config')


@babel.localeselector
def get_locale() -> Union[str, None]:
    '''Define get_locale'''
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GEt"], strict_slashes=False)
def hello_world() -> str:
    '''Define hello_world'''
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
