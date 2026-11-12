def count_even_digits(n):
    """Return how many decimal digits of n are even.

    n must be an exact built-in int in [0, 10**18]. Digits are taken
    from the decimal representation without leading zeros; 0 counts as
    an even digit, so count_even_digits(0) is 1.
    """
    if type(n) is not int:
        raise TypeError("n must be an exact built-in int")
    if n < 0 or n > 10**18:
        raise ValueError("n must be in [0, 10**18]")
    if n == 0:
        return 1
    count = 0
    while n > 0:
        if (n % 10) % 2 == 0:
            count += 1
        n //= 10
    return count
