from itertools import permutations

def detect_anagrams(word,candidates):

    all_possibility = []
    for w in set(permutations(word.lower())):
        w = ''.join(w)
        if w != word.lower():
            all_possibility.append(w)

    results = []
    for w in candidates:
        if w.lower() in all_possibility:
            results.append(w)

    return results
