def is_pangram(sentence):
    sentence = sentence.replace(" ", "").lower()
    if not sentence:
        return False
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for letter in sentence:
        if letter in alphabets:
            alphabets = alphabets.replace(letter, "")
    return len(alphabets) == 0
