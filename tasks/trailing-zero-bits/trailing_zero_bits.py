def trailing_zero_bits(n):
    if type(n) is not int:
        raise TypeError("n must be an exact built-in int")
    if n < 1 or n > 10**18:
        raise ValueError("n must be in [1, 10**18]")
    return (n & -n).bit_length() - 1
