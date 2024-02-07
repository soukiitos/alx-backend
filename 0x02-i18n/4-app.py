#!/usr/bin/env python3
'''Force locale with URL parameter'''
from typing import Union
from flask import Flask, request
from flask_babel import Babel
from routes.routes_4 import app_routes
from config import Config


app = Flask(__name__)
babel = Babel(app)


app.config.from_object(Config)
app.register_blueprint(app_routes)


@babel.localeselector
def get_locale() -> Union[str, None]:
    '''Define get_locale'''
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")