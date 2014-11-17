#checks if a dna sequence it's is complement
def to_rna(sequence):
    #the RNA complements
    complements={'G':'C','C':'G','T':'A','A':'U'}
    complement=""
    for c in sequence:
        complement+=complements[c]

    return complement