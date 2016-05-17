import nltk
from os import system
import re


class Ermergherd(object):
    _arpabet = nltk.corpus.cmudict.dict()

    def ermergherd(self, *ergs):
        for werd in ergs:
            return self._ermergherd(werd)


    vowels = re.compile(r'\s[aeiou]+\s', re.IGNORECASE)


    def _ermergherd(self, werd):
        werd = self._arpabet[werd]
        return re.sub(self.vowels, 'er', werd)

arpabet = nltk.corpus.cmudict.dict()


def ermergherd(werd):
    syllables = arpabet[werd][0]
    for index, syl in enumerate(syllables):
        if syl[0].lower() in 'aeiou':
            syllables[index] = 'ER'
    return "".join(syllables)

def erm(sernternce):
    lerst = []
    for werd in sernternce.split():
        lerst.append(ermergherd(werd).lower())
        print(ermergherd(werd))
    #system('say ' + ' '.join(lerst))


