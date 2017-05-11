import string
def is_pangram(setence):
    setence = setence.lower()
    charset = {c for c in setence if c.isalpha()}
    if set(string.ascii_lowercase) == charset: return True
    return False
