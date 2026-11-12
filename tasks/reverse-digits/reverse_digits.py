def reverse_digits(n):
    """Return n with its decimal digits reversed, as an exact int.

    n must be an exact built-in int in [0, 10**18]. Trailing zeros of
    n become leading zeros of the reversal and disappear, so
    reverse_digits(120) is 21 and reverse_digits(0) is 0.
    """
    if type(n) is not int:
        raise TypeError("n must be an exact built-in int")
    if n < 0 or n > 10**18:
        raise ValueError("n must be in [0, 10**18]")
    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n //= 10
    return result
