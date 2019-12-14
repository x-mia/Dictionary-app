from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class WordForm(FlaskForm):
    word = StringField('Sisesta sõna', validators=[DataRequired(), Length(1, 64)])
    language = SelectField('Language', choices=[('est-svk', 'Eesti-Slovaki'), ('svk-est', 'Slovaki-Eesti')])
    submit = SubmitField('Tõlgi')
class SlovakWordForm(FlaskForm):
    word = StringField('Zadaj slovo', validators=[DataRequired(), Length(1, 64)])
    language = SelectField('Jazyk', choices=[('est-svk', 'Estónsko-Slovenský'), ('svk-est', 'Slovensko-Estónsky')])
    submit = SubmitField('Prelož')
