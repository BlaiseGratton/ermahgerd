import nltk


arpabet = nltk.corpus.cmudict.dict()

def prersers_werd(werd):
    serlaberls = arpabet[werd.lower()][0]
    return ''.join(map(trernsferm_serlerberl, serlaberls))

def ermahgerd(sernternce):
    return ' '.join([prersers_werd(werd) for werd in sernternce.split()])

def trernsferm_serlerberl(serlaberl):
    return 'ER' if serlaberl[0] in 'AEIOU' else serlaberl

