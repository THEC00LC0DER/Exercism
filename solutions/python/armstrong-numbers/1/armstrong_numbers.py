def is_armstrong_number(number):
    number = str(number)
    power = len(number)
    final = 0
    if number == "0": 
        return True
    for i in number:
        final += int(i)**power
    return str(final) == number
    