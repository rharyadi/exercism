import string
mapper = dict(zip(string.ascii_lowercase, string.ascii_lowercase[::-1]))

def mapping(c):
    if c.isalpha():
        return mapper[c.lower()]
    else:
        return c

def grouping(alist):
    for i in range(5,len(alist)+1,6):
        alist.insert(i,' ')

def encode(text):
    encoded = [mapping(c) for c in text if c.isalnum()]
    grouping(encoded)
    return ''.join(encoded)


def decode(text):
    decoded = [mapping(c) for c in text if c.isalnum()]
    return ''.join(decoded)
