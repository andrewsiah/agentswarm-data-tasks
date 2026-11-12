def is_repdigit(n):
    """Return True exactly when every decimal digit of n is the same.

    n must be an exact built-in int in [0, 10**18]. Single-digit
    numbers are trivially repdigits, so is_repdigit(0) is True, while
    is_repdigit(10) is False.
    """
    if type(n) is not int:
        raise TypeError("n must be an exact built-in int")
    if n < 0 or n > 10**18:
        raise ValueError("n must be in [0, 10**18]")
    digit = n % 10
    n //= 10
    while n > 0:
        if n % 10 != digit:
            return False
        n //= 10
    return True
