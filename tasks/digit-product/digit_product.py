def digit_product(n):
    """Return the product of all decimal digits of n.

    n must be an exact built-in int in [0, 10**18]. Any n containing a
    0 digit (including 0 itself) returns 0. Exact integer arithmetic only.
    """
    if type(n) is not int:
        raise TypeError("n must be an exact built-in int")
    if n < 0 or n > 10**18:
        raise ValueError("n must be in [0, 10**18]")
    if n == 0:
        return 0
    result = 1
    while n > 0:
        result *= n % 10
        if result == 0:
            return 0
        n //= 10
    return result
