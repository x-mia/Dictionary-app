from pandas import read_csv
from difflib import get_close_matches
from collections import namedtuple

Entry = namedtuple('Entry', 'est_word est_postag svk_words svk_postags score sagedus sg_gen sg_part sg_ill short_ill pl_part da_inf first_pers impers vocabulary sonaveeb shapes')

def get_entry(est_word_group):

    est_word_group = est_word_group.sort_values(by="Skoor", ascending=False)
    first_row = est_word_group.iloc[0]

    entry = Entry(est_word=first_row["Eesti sõna"], est_postag=first_row["Est. sõnaliik"],
    svk_words=est_word_group["Slovaki sõna"].tolist(), svk_postags=est_word_group["Slov. sõnaliik"].tolist(), score=est_word_group["Skoor"].tolist(),
    sagedus=first_row["Sagedus"], sg_gen=first_row["SG GEN"], sg_part=first_row["SG PART"],
    sg_ill=first_row["SG ILL"], short_ill=first_row["SHORT ILL"], pl_part=first_row["PL PART"],
    da_inf=first_row["DA INF"], first_pers=first_row["1.isik aktiiv"], impers=first_row["Impersonaal"],
    vocabulary=first_row["Põhisõnavara esinev"], sonaveeb=first_row["Sõnaveeb"], shapes=first_row["Shapes"])

    return entry

def get_meaning(w, data):
    w = w.lower()
    data["Lowercase"] = data["Eesti sõna"].str.lower()
    gb = data.groupby("Lowercase")

    findings = [key for key in gb.groups.keys() if w in key]
    close_matches = get_close_matches(w, data["Eesti sõna"])

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
