def is_automorphic(n):
    """Return True exactly when n * n ends with the decimal digits of n.

    n must be an exact built-in int in [0, 10**15]. With k the number
    of decimal digits of n, this is (n * n) % 10**k == n, computed
    with exact integer arithmetic, so 25 and 76 are True, 10 is False
    and 0 is True.
    """
    if type(n) is not int:
        raise TypeError("n must be an exact built-in int")
    if n < 0 or n > 10**15:
        raise ValueError("n must be in [0, 10**15]")
    modulus = 10
    while modulus <= n:
        modulus *= 10
    return (n * n) % modulus == n
