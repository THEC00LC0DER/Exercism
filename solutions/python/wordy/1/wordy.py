from itertools import zip_longest
def answer(question):
    question = question[8:-1].replace(" by", "").split()
    length = len(question)
    if length == 1:
        return int(question[0])
    if length == 0 or question[0].isalpha():
        raise ValueError("syntax error")
    operated_value = int(question[0])
    valid_operations = "multiplied plus minus divided" # Whitespace added for readability
    flag = False
    for operator, operating_number in zip_longest(question[1::2], question[2::2]):
        if operator not in valid_operations:
            if operator.isnumeric() or operator is None:
                raise ValueError("syntax error")
            else:
                raise ValueError("unknown operation")
        try:
            if operating_number is None:
                raise ValueError("syntax error")
            operating_number = int(operating_number)
        except ValueError:
            raise ValueError("syntax error")
        match operator:
            case "multiplied":
                operated_value *= operating_number
            case "plus":
                operated_value += operating_number
            case "divided":
                operated_value /= operating_number
            case "minus":
                operated_value -= operating_number
    return operated_value