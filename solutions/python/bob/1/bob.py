def response(hey_bob):
    hey_bob = "".join(x for x in hey_bob if x.isalnum() or x == "?").strip()
    if not hey_bob:
        return "Fine. Be that way!"
    
    is_question = hey_bob.endswith("?")
    is_shouting = hey_bob.isupper() and any(c.isalpha() for c in hey_bob)

    if is_shouting and is_question:
        return "Calm down, I know what I'm doing!"
    if is_question:
        return "Sure."
    if is_shouting:
        return "Whoa, chill out!"
    return "Whatever."

print(response("1, 2, 3 GO!"))
