import string

def rotate(text,rot):
    lower_map = dict(zip(
                string.ascii_lowercase,
                string.ascii_lowercase[rot:26] + string.ascii_lowercase[0:rot]
                ))
    upper_map = dict(zip(
                string.ascii_uppercase,
                string.ascii_uppercase[rot:26] + string.ascii_uppercase[0:rot]
                ))

    rotated_text = []
    for c in text:
        if c.islower():
            c = lower_map[c]
        if c.isupper():
            c = upper_map[c]
        rotated_text.append(c)

    return ''.join(rotated_text)
