def leap_year(year):
    isLeapYear = True if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0 else False
    return isLeapYear