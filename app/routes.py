from app import app
from flask import render_template, url_for, redirect, flash
from app.forms import WordForm
from app.word_finding import get_meaning
from pandas import read_csv


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = WordForm()
    if form.validate_on_submit():
        return redirect(url_for('dictionary', word=form.word.data))
    return render_template('index.html', form=form)

@app.route('/dictionary/<word>')
def dictionary(word):
    data = read_csv("sonaraamat4.csv")
    entry = get_meaning(word, data)
    if not entry:
        return render_template('404.html', word=word, entry=entry)
    return render_template('dictionary.html', word=word, entry=entry)
