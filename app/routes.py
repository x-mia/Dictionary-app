from app import app
from flask import render_template, url_for, redirect, flash
from app.forms import WordForm, SlovakWordForm
from app.word_finding import get_meaning
from app.svk_wordfinding import get_svkmeaning
from pandas import read_csv


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = WordForm()
    if form.validate_on_submit():
        return redirect(url_for('dictionary', word=form.word.data, language=form.language.data))
    return render_template('index.html', form=form)

@app.route('/base_svk', methods=['GET', 'POST'])
def base_svk():
    form = SlovakWordForm()
    if form.validate_on_submit():
        return redirect(url_for('dictionary_svk', word=form.word.data, language=form.language.data))
    return render_template('base-svk.html', form=form)

@app.route('/dictionary/<language>/<word>')
def dictionary(word, language):
    form = WordForm()
    if form.validate_on_submit():
        return redirect(url_for('dictionary', word=form.word.data, language=form.language.data))

    data = read_csv("sonastik.csv")
    if language == "est-svk":
        entry = get_meaning(word, data)
        if not entry:
            return render_template('404.html', form=form, word=word, entry=entry)
        return render_template('dictionary.html', form=form, word=word, entry=entry)
    if language == "svk-est":
        entry = get_svkmeaning(word, data)
        if not entry:
            return render_template('404.html', form=form, word=word, entry=entry)
        return render_template('language.html', form=form, word=word, entry=entry)


@app.route('/dictionary_svk/<language>/<word>')
def dictionary_svk(word, language):
    form = SlovakWordForm()
    if form.validate_on_submit():
        return redirect(url_for('dictionary_svk', word=form.word.data, language=form.language.data))

    data = read_csv("sonastik.csv")
    if language == "est-svk":
        entry = get_meaning(word, data)
        if not entry:
            return render_template('404-svk.html', form=form, word=word, entry=entry)
        return render_template('dictionary-svk.html', form=form, word=word, entry=entry)
    if language == "svk-est":
        entry = get_svkmeaning(word, data)
        if not entry:
            return render_template('404-svk.html', form=form, word=word, entry=entry)
        return render_template('language-svk.html', form=form, word=word, entry=entry)
