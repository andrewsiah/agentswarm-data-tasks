def digit_sum(n):
    if type(n) is not int:
        raise TypeError("n must be an exact built-in int")
    if n < -1000000000000000000 or n > 1000000000000000000:
        raise ValueError("n must be in [-1000000000000000000, 1000000000000000000]")
    total = 0
    m = -n if n < 0 else n
    while m:
        total += m % 10
        m //= 10
    return total
