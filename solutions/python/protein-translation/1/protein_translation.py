def proteins(strand):
    codon_dict = {'Methionine':['AUG'], 'Phenylalanine':['UUU', 'UUC'], 'Leucine':['UUA', 'UUG'], 'Serine': ['UCU', 'UCC', 'UCA', 'UCG'], 'Tyrosine':['UAU', 'UAC'], 'Cysteine' : ['UGU', 'UGC'], 'Tryptophan' :['UGG']}
    STOP = ["UAA", "UAG", "UGA"]
    
    codons = ''
    protein_list = []
    for char in strand:
        codons += char
        print(codons)
        if len(codons) == 3:
            if codons in STOP:
                return protein_list
            for value in codon_dict:
                if codons in codon_dict[value]:
                    protein_list.append(value)
            codons = ''
        
    return protein_list
