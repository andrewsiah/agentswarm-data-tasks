def is_leap_year(year):
    if type(year) is not int:
        raise TypeError('exact integer required')
    if year < 1:
        raise ValueError('year must be at least 1')
    return False
