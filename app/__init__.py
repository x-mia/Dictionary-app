from flask import Flask, g, request
from config import Config
from flask_bootstrap import Bootstrap
from flask_babel import Babel


app = Flask(__name__)
app.config.from_object(Config)

from app import routes

bootstrap = Bootstrap(app)
babel = Babel(app)

@babel.localeselector
def get_locale():
    return g.get('current_lang', 'ee')

@app.before_request
def before():
    if request.view_args and 'lang_code' in request.view_args:
        if request.view_args['lang_code'] not in ('ee', 'sk'):
            return abort(404)
        g.current_lang = request.view_args['lang_code']
        request.view_args.pop('lang_code')
