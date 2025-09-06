def square(number):
    if number > 64 or number < 1 or number != int(number):
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)

def total():
    return sum([2**(x-1) for x in range(1,64+1)])