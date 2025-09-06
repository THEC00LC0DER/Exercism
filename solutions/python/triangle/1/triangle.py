def isTriangle(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a+b>=c and b+c>=a  and a + c >= b and a != 0:
        return True
    return False

def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if not isTriangle(sides):
        return False
    if a == b and b == c and a == c:
        return True
    return False


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if not isTriangle(sides):
        return False
    if (a == b) or (b == c) or (a == c):
        return True
    return False


def scalene(sides):
    if not isTriangle(sides) or equilateral(sides) or isosceles(sides):
        return False
    return True
