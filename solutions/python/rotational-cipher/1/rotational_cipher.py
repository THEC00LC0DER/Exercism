from string import ascii_lowercase, ascii_uppercase


def rotate(text, key):
    if key == 0 or key == 26 or not 1 <= key <= 25:
        return text
    lowercase = ascii_lowercase
    uppercase = ascii_uppercase
    alphabet = ascii_lowercase + ascii_uppercase
    cipher = lowercase[-key:] + lowercase[:len(lowercase) - key] + uppercase[-key:] + uppercase[:len(uppercase) - key]
    table = str.maketrans(cipher, alphabet)
    return text.translate(table)
