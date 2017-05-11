def to_rna(seq):
    trans = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    rna = []
    for c in seq:
        try:
            rna.append(trans[c])
        except KeyError:
            return ''
    return ''.join(rna)
