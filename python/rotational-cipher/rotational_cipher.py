import string

def rotate(text,rot):
    lower_map = dict(zip(
                string.ascii_lowercase,
                string.ascii_lowercase[rot:] + string.ascii_lowercase[:rot]
                ))
    upper_map = dict(zip(
                string.ascii_uppercase,
                string.ascii_uppercase[rot:] + string.ascii_uppercase[:rot]
                ))

    charmap = {**lower_map, **upper_map}

    rotated_text = []

    for c in text:
        rotated_text.append(charmap.get(c,c))

    return ''.join(rotated_text)
