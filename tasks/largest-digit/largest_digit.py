def largest_digit(n):
    if type(n) is not int:
        raise TypeError("n must be an exact built-in int")
    if n < 0 or n > 10**18:
        raise ValueError("n must be in [0, 10**18]")
    best = 0
    m = n
    while m:
        d = m % 10
        if d > best:
            best = d
            if best == 9:
                break
        m //= 10
    return best
