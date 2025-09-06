from string import ascii_lowercase


def encode(plain_text):
    alphabet = ascii_lowercase
    cipher_text = alphabet[::-1]
    plain_text = returnTranslatedString(alphabet, cipher_text, plain_text.lower())
    return " ".join(plain_text[index:index+5] for index in range(0, len(plain_text), 5))


def returnTranslatedString(translate_characters, cipher_characters, plain_text):
    table = str.maketrans(translate_characters, cipher_characters, " .,")
    return plain_text.translate(table)


def decode(ciphered_text):
    alphabet = ascii_lowercase
    exchange_cipher = alphabet[::-1]
    return returnTranslatedString(exchange_cipher, alphabet, ciphered_text)