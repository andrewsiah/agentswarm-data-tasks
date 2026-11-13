def count_distinct_digits(n):
    if type(n) is not int:
        raise TypeError()

    if n < 0 or n > 10**18:
        raise ValueError()

    return len(set(str(n)))