def is_harshad(n):
    """Return True exactly when n is divisible by its decimal digit sum.

    n must be an exact built-in int in [1, 10**18]. Only integer
    arithmetic is used (the % operator, never float division), so the
    answer is exact up to 10**18: 12 and 18 are True, 11 and 19 are
    False.
    """
    if type(n) is not int:
        raise TypeError("n must be an exact built-in int")
    if n < 1 or n > 10**18:
        raise ValueError("n must be in [1, 10**18]")
    digit_sum = 0
    rest = n
    while rest > 0:
        digit_sum += rest % 10
        rest //= 10
    return n % digit_sum == 0
