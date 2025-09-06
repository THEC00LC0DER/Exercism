def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    list_new = []
    for index in range(1, number, 1):
        if number % index == 0:
            list_new.append(index)
    if sum(list_new) == number:
        return "perfect"
    elif sum(list_new) > number:
        return "abundant"
    return "deficient"