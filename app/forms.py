from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from flask_babel import lazy_gettext as _l

class WordForm(FlaskForm):
    word = StringField(_l('Sisesta sõna'), validators=[DataRequired(), Length(1, 64)])
    language = SelectField('Language', choices=[('est-svk', _l('Eesti-Slovaki')), ('svk-est', _l('Slovaki-Eesti'))])
    submit = SubmitField(_l('Tõlgi'))
