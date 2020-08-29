from flask import Flask, g, request, abort
from config import Config
from flask_bootstrap import Bootstrap
from flask_babel import Babel
from pandas import read_csv


app = Flask(__name__)
app.config.from_object(Config)

data = read_csv("sonastik.csv")
data["Lowercase_est"] = data["Eesti sõna"].str.lower()
data["Lowercase_svk"] = data["Slovaki sõna"].str.lower()
gb_est = data.groupby("Lowercase_est")
gb_svk = data.groupby("Lowercase_svk")

from app import routes

bootstrap = Bootstrap(app)
babel = Babel(app, default_locale="ee")

@babel.localeselector
def get_locale():
    return g.get('current_lang', 'ee')

@app.before_request
def before():
    if request.view_args and 'lang_code' in request.view_args:
        if request.view_args['lang_code'] not in ('ee', 'sk'):
            return abort(404)
        g.current_lang = request.view_args['lang_code']
