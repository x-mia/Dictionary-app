import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    LANGUAGES = ['ee', 'sk']
    BABEL_DEFAULT_LOCALE = "ee"
