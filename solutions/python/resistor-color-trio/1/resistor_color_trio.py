def label(colors):
    color_dict = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7,
                  "grey": 8, "white": 9}

    number = (color_dict[colors[1]] + color_dict[colors[0]] * 10)
    power =  10 ** color_dict[colors[2]]
    this_var = str(number * power)
    number_of_zeros = len(this_var[this_var.index("0"):]) if this_var.endswith("0") else 0
    if number_of_zeros < 3:
        return  str(number * power) + " ohms"
    elif number_of_zeros < 6:
        return str(number * power // 10 ** 3) +  " kiloohms"
    elif number_of_zeros <  9:
        return str(number * power // 10 ** 6) +  " megaohms"
    else:
        return str(number) + " gigaohms"


