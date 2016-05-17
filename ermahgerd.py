from hyphenator import Hyphenator
import re


hyph = Hyphenator("./hyph_nl_NL.dic")

vowels = ['a', 'e', 'i', 'o', 'u', 'y',
          'aa', 'ae', 'ai', 'ao', 'au', 
          'ea', 'ee', 'ei', 'eo', 'eu', 
          'ia', 'ie', 'ii', 'io', 'iu', 
          'oa', 'oe', 'oi', 'oo', 'ou', 
          'ua', 'ue', 'ui', 'uo', 'uu',
         ]

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
              'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

regex_vowels = '|'.join(vowels)
regex_consonants = '|'.join(consonants)

def ermahgerd(input):
    words = input.split(' ')
    ermahgerded_werds = []
    for word in words:
        syllables = hyph.inserted(word).split('-')
        if word.lower() == "facebook":
            syllables = ['face', 'book']
        ermahgerded_serllerberls = [process_syllable(s) for s in syllables]
        rerplerced = ''.join(ermahgerded_serllerberls)
        if 'erer' in rerplerced:
            rerplerced = rerplerced.replace('erer', 'er')
        if 'erer' in rerplerced:
            rerplerced = rerplerced.replace('erer', 'err')
        if rerplerced[-3:] == 'erl':
            rerplerced = rerplerced[:len(rerplerced)-1]
        ermahgerded_werds.append(rerplerced)
    return ' '.join(ermahgerded_werds)


def process_syllable(syllable):
    vowel, initial_consonant, middle_consonant = find_vowel(syllable)
    if middle_consonant != '':
        if middle_consonant == 'c':
            middle_consonant = 's'
        rerplerced = initial_consonant + 'er' + middle_consonant
    else:
        rerplerced = syllable.replace(vowel, 'er')
    return rerplerced


def find_vowel(syllable):
    initial_consonant = ''
    middle_consonant = ''

    # ad-hoc cases:
    if syllable == 'le':
        return 'le', initial_consonant, middle_consonant
    if 'oy' in syllable:
        return 'o', initial_consonant, middle_consonant
    if 'ough' in syllable:
        return 'e', '', 'f'

    # e.g. "face", "ace", "one", "ate":
    vowel = ''
    if re.match(r'([{0}]?([{1}]+[{2}]+[{3}]+)+)+'.format(
            regex_consonants, regex_vowels, regex_consonants, regex_vowels
        ), syllable):
        if syllable[0] in vowels:
            for c in syllable:
                if c not in vowels:
                    middle_consonant += c
        else:
            initial = True
            for c in syllable:
                if c in consonants and initial:
                    initial_consonant += c
                elif c in consonants and not initial:
                    middle_consonant += c
                if c in vowels:
                    initial = False

    # general cases:
    else:
        for v in vowels:
            if syllable.find(v) > -1:
                vowel = v
    return vowel, initial_consonant, middle_consonant
