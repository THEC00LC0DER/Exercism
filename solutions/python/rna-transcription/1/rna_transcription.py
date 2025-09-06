def to_rna(dna_strand) -> str:
    rna = ''
    for nucleotide in dna_strand:
        if nucleotide == 'G':
            rna += 'C'
        elif nucleotide == 'T':
            rna += 'A'
        elif nucleotide == 'A':
            rna += 'U'
        elif nucleotide == 'C':
            rna += 'G'
    return rna
