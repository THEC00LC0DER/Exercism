def is_isogram(string):
    string = [character.lower() for character in string if character.isalpha()]
    return len(string) == len(set(string))
