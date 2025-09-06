def factors(value):
    num = 2
    prime = []
    while value != 1:
        while value % num == 0:
            prime.append(num)
            value /= num
        num += 1
    return prime
