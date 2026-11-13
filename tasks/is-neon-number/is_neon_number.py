def is_neon_number(n):
    if type(n) is not int:
        raise TypeError()

    if n < 0 or n > 10**18:
        raise ValueError()

    return sum(int(d) for d in str(n * n)) == n