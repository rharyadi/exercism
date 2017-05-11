from collections import Counter

def word_count(s):
    sentence = ''.join([c if c.isalnum() else ' ' for c in s.lower()])
    wordlist = sentence.split()
    return dict(Counter(wordlist))
    
