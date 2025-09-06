from string import ascii_lowercase


def encode(plain_text):
    alphabet = list(ascii_lowercase)
    exchange_cipher = "zyxwvutsrqponmlkjihgfedcba"
    #joins seperated in order to not make clunky
    plain_text = "".join(letter.lower() for letter in plain_text if letter.isalpha() or letter.isdigit()) # remove extra characters
    plain_text = "".join(exchange_cipher[alphabet.index(character)] if character.isalpha() else character for character in plain_text)
    return "".join(letter if (index + 1) % 5 != 0 else letter + " " for index, letter in enumerate(plain_text)).rstrip()


def decode(ciphered_text):
    alphabet = list(ascii_lowercase)
    exchange_cipher = "zyxwvutsrqponmlkjihgfedcba"
    ciphered_text = ciphered_text.replace(" ", "")
    return "".join(alphabet[exchange_cipher.index(character)] if character.isalpha() else character for character in ciphered_text)