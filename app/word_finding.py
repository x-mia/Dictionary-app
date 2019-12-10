from pandas import read_csv
from difflib import get_close_matches
from collections import namedtuple

Entry = namedtuple('Entry', 'est_word est_postag svk_words svk_postags score sagedus sg_gen sg_part sg_ill short_ill pl_part da_inf first_pers impers vocabulary sonaveeb')

# data = read_csv("sonaraamat4.csv")

# word = input("Enter word: ")

def get_meaning(w, data):
    w = w.lower()
    if any(data["Eesti sõna"].isin([w])):
        df = data[data["Eesti sõna"] == w]
        first_row = df.iloc[0]
        entry = Entry(est_word=first_row["Eesti sõna"], est_postag=first_row["Est. sõnaliik"],
        svk_words=df["Slovaki sõna"].tolist(), svk_postags=df["Slov. sõnaliik"].tolist(), score=first_row["Skoor"],
        sagedus=first_row["Sagedus"], sg_gen=first_row["SG GEN"], sg_part=first_row["SG PART"],
        sg_ill=first_row["SG ILL"], short_ill=first_row["SHORT ILL"], pl_part=first_row["PL PART"],
        da_inf=first_row["DA INF"], first_pers=first_row["1.isik aktiiv"], impers=first_row["Impersonaal"],
        vocabulary=first_row["Põhisõnavara esinev"], sonaveeb=first_row["Sõnaveeb"])
        return entry

    elif len(get_close_matches(w, data["Eesti sõna"])) > 0:
        close_match = get_close_matches(w, data["Eesti sõna"])[0]
        df = data[data["Eesti sõna"] == close_match]
        first_row = df.iloc[0]
        entry = Entry(est_word=first_row["Eesti sõna"], est_postag=first_row["Est. sõnaliik"],
        svk_words=df["Slovaki sõna"].tolist(), svk_postags=df["Slov. sõnaliik"].tolist(), score=first_row["Skoor"],
        sagedus=first_row["Sagedus"], sg_gen=first_row["SG GEN"], sg_part=first_row["SG PART"],
        sg_ill=first_row["SG ILL"], short_ill=first_row["SHORT ILL"], pl_part=first_row["PL PART"],
        da_inf=first_row["DA INF"], first_pers=first_row["1.isik aktiiv"], impers=first_row["Impersonaal"],
        vocabulary=first_row["Põhisõnavara esinev"], sonaveeb=first_row["Sõnaveeb"])
        return entry

    else:
        print("The word doesn't exist.")


# meaning = get_meaning(word, data)
#
# print("Meaning: " , meaning)
