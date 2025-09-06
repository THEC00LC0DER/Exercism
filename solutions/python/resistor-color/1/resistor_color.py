def color_code(color):
    colors_value = {color: value for value, color in enumerate(colors())}
    return colors_value[color]

def colors():
    color_list = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]
    return color_list
