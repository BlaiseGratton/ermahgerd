import nltk
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



def ermergherd(werd):
    arpabet = nltk.corpus.cmudict.dict()
    syllables = arpabet[werd][0]
    for index, syl in enumerate(syllables):
        if syl[0].lower() in 'aeiou':
            syllables[index] = 'ER'
    return "".join(syllables)

