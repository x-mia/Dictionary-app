from app import app
from flask import render_template, url_for, redirect, flash
from app.forms import WordForm, SlovakWordForm
from app.word_finding import get_meaning
from pandas import read_csv


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = WordForm()
    if form.validate_on_submit():
        return redirect(url_for('dictionary', word=form.word.data))
    return render_template('index.html', form=form)

@app.route('/base_svk', methods=['GET', 'POST'])
def base_svk():
    form = SlovakWordForm()
    if form.validate_on_submit():
        return redirect(url_for('dictionary_svk', word=form.word.data))
    return render_template('base-svk.html', form=form)

@app.route('/dictionary/<word>')
def dictionary(word):
    form = WordForm()
    if form.validate_on_submit():
        return redirect(url_for('dictionary', form=form, word=form.word.data))

    data = read_csv("sonastik.csv")
    entry = get_meaning(word, data)
    if not entry:
        return render_template('404.html', form=form, word=word, entry=entry)
    return render_template('dictionary.html', form=form, word=word, entry=entry)

@app.route('/dictionary_svk/<word>')
def dictionary_svk(word):
    form = SlovakWordForm()
    if form.validate_on_submit():
        return redirect(url_for('dictionary_svk', form=form, word=form.word.data))

    data = read_csv("sonastik.csv")
    entry = get_meaning(word, data)
    if not entry:
        return render_template('404-svk.html', form=form, word=word, entry=entry)
    return render_template('dictionary-svk.html', form=form, word=word, entry=entry)
