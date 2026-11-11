def is_leap_year(year):
    if type(year) is not int:
        raise TypeError('exact integer required')
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
