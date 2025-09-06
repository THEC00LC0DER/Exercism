def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(value != strand_b[index] for index, value in enumerate(strand_a))