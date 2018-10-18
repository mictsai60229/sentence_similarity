import itertools, unicodedata
import re


def group_words(s):
    regex = []

    # Match a whole word:
    regex += [r'\w+']

    # Match a single CJK character:
    regex += [r'[\u4e00-\ufaff]']

    # Match one of anything else, except for spaces:
    regex += [r'[^\s]']

    regex = "|".join(regex)
    r = re.compile(regex, re.ASCII)

    return r.findall(s)


def character_splitter(line):
    return " ".join(group_words(str(line)))




def line_splitter(paragraph):
    for sent in re.findall(u'[^!?。，\.\!\?]+[!?。，\.\!\?]?', paragraph, flags=re.U):
        yield sent