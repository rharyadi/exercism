from itertools import groupby

def decode():
    pass


def encode(msg):
    encoded = []
    for k,g in groupby(msg):
        length = len(list(g))
        if length > 1:
            encoded.append(str(length))
        encoded.append(k)
    return ''.join(encoded)

