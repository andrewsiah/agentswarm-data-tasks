def factorial_zeros(n):
    if type(n) is not int:
        raise TypeError("n must be an exact int")
    if n < 0 or n > 10**18:
        raise ValueError("n must be in [0, 10**18]")
    zeros = 0
    power = 5
    while power <= n:
        zeros += n // power
        power *= 5
    return zeros
