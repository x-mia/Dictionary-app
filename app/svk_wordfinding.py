from pandas import read_csv
from difflib import get_close_matches
from collections import namedtuple

Entry = namedtuple('Entry', 'svk_word svk_postag est_words')


def get_svkmeaning(w, data):
    w = w.lower()
    if any(data["Slovaki sõna"].isin([w])):
        df = data[data["Slovaki sõna"] == w]
        df = df.sort_values(by="Skoor", ascending=False)
        first_row = df.iloc[0]
        entry = Entry(svk_word=first_row["Slovaki sõna"], svk_postag=first_row["Slov. sõnaliik"], est_words=df["Eesti sõna"].tolist())
        return entry

    elif len(get_close_matches(w, data["Slovaki sõna"])) > 0:
        close_match = get_close_matches(w, data["Slovaki sõna"])[0]
        df = data[data["Slovaki sõna"] == close_match]
        df = df.sort_values(by="Skoor", ascending=False)
        first_row = df.iloc[0]
        entry = Entry(svk_word=first_row["Slovaki sõna"], svk_postag=first_row["Slov. sõnaliik"], est_words=df["Eesti sõna"].tolist())
        return entry

    else:
        print("The word doesn't exist.")
