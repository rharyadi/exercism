def abbreviate(longphrase):
    longphrase = longphrase.replace('-',' ')
    abbr = [w[0].upper() for w in longphrase.split()]
    return ''.join(abbr)
