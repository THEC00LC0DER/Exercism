def response(hey_bob):
    response = "Whatever."
    hey_bob = hey_bob.strip()
    if not hey_bob:  
        response = "Fine. Be that way!" 
    if hey_bob.isupper() and hey_bob.endswith('?'):
        return "Calm down, I know what I'm doing!"
    if hey_bob.isupper():
        response = "Whoa, chill out!"
    if hey_bob.endswith('?'):
        response = "Sure."
    return response