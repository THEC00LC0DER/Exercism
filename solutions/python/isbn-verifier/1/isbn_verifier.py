def is_valid(isbn: str) -> bool:
    isbn = isbn.replace("-", "")
    if len(isbn) != 10 or (not isbn[-1].isnumeric() and isbn[-1] != "X") or not isbn[:-1].isnumeric():
        return False
    last_digit: int = int(isbn[9]) if isbn[9] != "X" else 10
    isbn = isbn[:-1]
    check_digit: int = sum([int(char) * (10 - index) for index, char in enumerate(isbn)]) + last_digit
    return  check_digit % 11 == 0