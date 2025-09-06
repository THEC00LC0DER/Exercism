def reverse(text):
    reversed_string = ""
    text = text.strip()
    for i in range(len(text)):
        reversed_string += text[-i-1]
    return reversed_string