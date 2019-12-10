from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class WordForm(FlaskForm):
    word = StringField('Sisesta sõna', validators=[DataRequired()])
    submit = SubmitField('Tõlgi')
