def is_pangram(sentence):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    return all(letter in sentence.lower() for letter in alphabets)
