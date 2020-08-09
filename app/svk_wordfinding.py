from pandas import read_csv
from difflib import get_close_matches
from collections import namedtuple

Entry = namedtuple('Entry', 'svk_word svk_postag est_words')


def get_entry(svk_word_group):

    svk_word_group = svk_word_group.sort_values(by="Skoor", ascending=False)
    first_row = svk_word_group.iloc[0]

    entry = Entry(svk_word=first_row["Slovaki sõna"], svk_postag=first_row["Slov. sõnaliik"], est_words=svk_word_group["Eesti sõna"].tolist())

    return entry

def get_svkmeaning(w, data):
    w = w.lower()
    data["Lowercase"] = data["Slovaki sõna"].str.lower()
    gb = data.groupby("Lowercase")

    findings = [key for key in gb.groups.keys() if w in key]
    close_matches = get_close_matches(w, data["Slovaki sõna"])

    if w in gb.groups:
        entry = get_entry(gb.get_group(w))
    elif any([w in key for key in gb.groups.keys()]):
        entry = get_entry(gb.get_group(findings[0]))
    elif len(close_matches) > 0:
        entry = get_entry(gb.get_group(close_matches[0]))
    else:
        entry = None

    other_found_words = []
    for word in findings:
        finding = get_entry(gb.get_group(word))
        other_found_words.append(finding)

    other_close_matches = []
    for word in close_matches:
        close_match = get_entry(gb.get_group(word))
        other_close_matches.append(close_match)

    return entry, other_found_words, other_close_matches
