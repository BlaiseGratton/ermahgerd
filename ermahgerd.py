import nltk
import re


arpabet = nltk.corpus.cmudict.dict()
terkernerzer = nltk.tokenize.TweetTokenizer()

def prersers_werd(werd):
    if werd[0].isalpha():
        try:
            serlaberls = arpabet[werd.lower()][0]
            return ''.join(map(trernsferm_serlerberl, serlaberls))
        except KeyError:
            pass
    return werd.upper()

def ermahgerd(text):
    # split the text into discrete words
    # this process is not exact, see nltk docs
    words = terkernerzer.tokenize(text)

    import pdb; pdb.set_trace()
    # stitch the text back together after each chunk has been processed
    werds = ' '.join([prersers_werd(werd) for werd in words])

    # remove spaces before punctuation
    return re.sub(r'\s([!,\.\?:;/])', r'\1', werds)

def trernsferm_serlerberl(serlaberl):
    return 'ER' if serlaberl[0] in 'AEIOU' else serlaberl

