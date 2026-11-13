def is_disarium(n):
    if type(n) is not int:
        raise TypeError()

    if n < 0 or n > 10**18:
        raise ValueError()

    return sum(int(d) ** i for i, d in enumerate(str(n), 1)) == n