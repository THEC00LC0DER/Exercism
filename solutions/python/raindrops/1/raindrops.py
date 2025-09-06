def convert(number):
    this_str = ""
    if not number % 3:
        this_str += "Pling"
    if not number % 5:
        this_str += "Plang"
    if not number % 7:
        this_str += "Plong"
    return str(number) if not this_str else this_str