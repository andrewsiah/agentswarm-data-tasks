def digit_range(n):
    if type(n) is not int:
        raise TypeError()

    if n < 0 or n > 10**18:
        raise ValueError()

    digits = str(n)
    return int(max(digits)) - int(min(digits))