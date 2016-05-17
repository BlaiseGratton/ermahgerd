from hyphenator import Hyphenator
hyph = Hyphenator("./hyph_nl_NL.dic")


def ermahgerd(input):
    syllables = hyph.inserted(input).split('-')
    
    return ''.join(syllables)
