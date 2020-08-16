from app import app
from flask import render_template, url_for, redirect, flash, request
from app.forms import WordForm, SlovakWordForm
from app.word_finding import get_meaning
from pandas import read_csv


data = read_csv("sonastik.csv")

@app.route('/')
def root():
    print(app.config['BABEL_DEFAULT_LOCALE'])
    return redirect(url_for('index', lang_code='ee'))

@app.route('/index/<lang_code>', methods=['GET', 'POST'])
def index():
    form = WordForm()
    if form.validate_on_submit():
        return redirect(url_for('dictionary', word=form.word.data, language=form.language.data))
    return render_template('index.html', form=form)

@app.route('/<lang_code>/dictionary/<language>/<word>')
def dictionary(word, language):
    form = WordForm()
    if form.validate_on_submit():
        return redirect(url_for('dictionary', word=form.word.data, language=form.language.data))

    entry, other_found_words, other_close_matches = get_meaning(word, data, language)
    if not entry:
        return render_template('404.html')
    return render_template('dictionary.html', form=form, word=word, entry=entry,
                            other_found_words=other_found_words, other_close_matches=other_close_matches, language=language)

# @app.route('/base_svk', methods=['GET', 'POST'])
# def base_svk():
#     form = SlovakWordForm()
#     if form.validate_on_submit():
#         return redirect(url_for('dictionary_svk', word=form.word.data, language=form.language.data))
#     return render_template('base-svk.html', form=form)
#
# @app.route('/dictionary_svk/<language>/<word>')
# def dictionary_svk(word, language):
#     form = SlovakWordForm()
#     if form.validate_on_submit():
#         return redirect(url_for('dictionary_svk', word=form.word.data, language=form.language.data))
#
#     entry, other_found_words, other_close_matches = get_meaning(word, data, language)
#     if not entry:
#         return render_template('404-svk.html')
#         # # TODO:
#     return render_template('dictionary.html', form=form, word=word, entry=entry, other_found_words=other_found_words, other_close_matches=other_close_matches, language=language)
