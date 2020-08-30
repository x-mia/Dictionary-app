from difflib import get_close_matches
from collections import namedtuple


Entry = namedtuple('Entry', 'base_word postag translated_words score sonaveeb shapes')
EntrySVK = namedtuple('Entry', 'base_word postag translated_words')

def get_entry(word_group, language):

    word_group = word_group.sort_values(by="Skoor", ascending=False)
    first_row = word_group.iloc[0]

    if language == "est-svk":
        entry = Entry(base_word=first_row["Eesti sõna"], postag=first_row["Est. sõnaliik"],
        translated_words=word_group["Slovaki sõna"].tolist(), score=word_group["Skoor"].tolist(),
        sonaveeb=first_row["Sõnaveeb"], shapes=eval(first_row["Shapes"]))
    if language == "svk-est":
        entry = EntrySVK(base_word=first_row["Slovaki sõna"], postag=first_row["Slov. sõnaliik"], translated_words=word_group["Eesti sõna"].tolist())

    return entry

def get_meaning(w, gb, language):
    w = w.lower()

    findings = [key for key in gb.groups.keys() if w in key]

    close_matches = get_close_matches(w, gb.groups.keys())


    if w in gb.groups:
        entry = get_entry(gb.get_group(w), language)
    elif any([w in key for key in gb.groups.keys()]):
        entry = get_entry(gb.get_group(findings[0]), language)
    elif len(close_matches) > 0:
        entry = get_entry(gb.get_group(close_matches[0]), language)
    else:
        entry = None

    other_found_words = []
    for word in findings:
        finding = get_entry(gb.get_group(word), language)
        other_found_words.append(finding)

    other_close_matches = []
    for word in close_matches:
        close_match = get_entry(gb.get_group(word), language)
        other_close_matches.append(close_match)

    return entry, other_found_words, other_close_matches
