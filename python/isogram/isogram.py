def is_isogram(setring):
    setring = setring.lower()
    for c in setring:
        if setring.isalpha() and setring.count(c)>1:
            return False
    return True
