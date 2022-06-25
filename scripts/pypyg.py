from sre_parse import SPECIAL_CHARS

VOWELS = "aeiou"
VSUFFIX = "yay"
CSUFFIX = "ay"
CLUSTER = ['pl', 'pr', 'bl', 'br', 'tr', 'dr', 'kl', 'kr', 'gl',
           'gr', 'fl', 'fr', 'shr', 'sk', 'skr', 'sl', 'sm',
           'sn', 'sp', 'spl', 'spr', 'st', 'str', 'sw', 'tw',
           'dw', 'kw', 'skw', 'gw', 'qu', 'sch']


def pygify(string: str):
    rstring = ""
    for word in string.split(" "):
        word.strip(SPECIAL_CHARS)
        fLetter = word[0]
        f2Letters = word[:2]
        f3letters = word[:3]
        if fLetter.isupper():
            if f3letters.casefold() in CLUSTER:
                word = word[3:] + f3letters.lower() + CSUFFIX
            elif f2Letters.casefold() in CLUSTER:
                word = word[2:] + f2Letters.lower() + CSUFFIX
            elif fLetter.casefold() in VOWELS:
                word = word[1:] + fLetter.lower() + VSUFFIX
            else:
                word = word[1:] + fLetter.lower() + CSUFFIX
            word = word.capitalize()

        else:
            if word[:3].casefold() in CLUSTER:
                word = word[3:] + word[:3] + CSUFFIX
            elif word[:2].casefold() in CLUSTER:
                word = word[2:] + word[0:2] + CSUFFIX
            elif fLetter.casefold() in VOWELS:
                word = word[1:] + fLetter + VSUFFIX
            else:
                word = word[1:] + fLetter + CSUFFIX

        rstring += word + " "
    print(rstring)
    return rstring


def depygify():
    pass


pygify("Small big Olive spring Schedule")
