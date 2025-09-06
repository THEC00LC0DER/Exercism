def translate(text):
    text = text.strip()
    if " " in text:
        this_list = text.split()
        for index in range(len(this_list)):
            this_list[index] = translate(this_list[index])
        return " ".join(this_list)
    vowels = "aeiou"
    if text[0] in vowels or text[0:2] == "xr" or text[0:2] == "yt":
        return text + "ay"
    word_to_append = ""
    for index in range(len(text)):
        if text[index] == "y" and index != 0:
            return text.strip() + word_to_append + "ay"
        elif text[index] + text[index + 1] == "qu":
            return text.strip()[2:] + word_to_append + "qu" + "ay"
        elif text[index] in vowels:
            return text.strip() + word_to_append + "ay"
        word_to_append += text[index]
        text = text[:index] + " " + text[index+1:]
    return text + "ay"


