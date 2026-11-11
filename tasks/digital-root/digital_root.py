def digital_root(n):
    if type(n) is not int:
        raise TypeError("n must be an exact built-in int")
    if n < 0 or n > 10**18:
        raise ValueError("n must be in [0, 10**18]")
    while n >= 10:
        total = 0
        m = n
        while m:
            total += m % 10
            m //= 10
        n = total
    return n
