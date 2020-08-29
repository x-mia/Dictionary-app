from app import app
from flask import render_template, url_for, redirect, flash, request
from app.forms import WordForm
from app.word_finding import get_meaning
from pandas import read_csv



data = read_csv("sonastik.csv")
data["Lowercase_est"] = data["Eesti sõna"].str.lower()
data["Lowercase_svk"] = data["Slovaki sõna"].str.lower()
gb_est = data.groupby("Lowercase_est")
gb_svk = data.groupby("Lowercase_svk")


@app.route('/')
def root():
    return redirect(url_for('index', lang_code='ee'))

@app.route('/index/<lang_code>', methods=['GET', 'POST'])
def index(lang_code):
    form = WordForm()
    if form.validate_on_submit():
        return redirect(url_for('dictionary', word=form.word.data, language=form.language.data, lang_code=lang_code))
    return render_template('index.html', form=form, lang_code=lang_code)

@app.route('/dictionary/<language>/<word>/<lang_code>')
def dictionary(word, language, lang_code):
    form = WordForm(language=language)
    if form.validate_on_submit():
        return redirect(url_for('dictionary', word=form.word.data, language=form.language.data, lang_code=lang_code))
    if language == "est-svk":
        gb = gb_est
    elif language == "svk-est":
        gb = gb_svk

    entry, other_found_words, other_close_matches = get_meaning(word, gb, language)
    if not entry:
        return render_template('404.html', form=form, lang_code=lang_code)
    return render_template('dictionary.html', form=form, word=word, entry=entry,
                            other_found_words=other_found_words, other_close_matches=other_close_matches, language=language, lang_code=lang_code)
