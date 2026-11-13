from math import isqrt

MAX_VALUE = 10**12


def is_prime(n):
    # Exact-type check first: rejects bool and int subclasses.
    if type(n) is not int:
        raise TypeError("n must be an int")
    if n < 0 or n > MAX_VALUE:
        raise ValueError("n must be in [0, 10**12]")

    if n < 2:
        return False
    if n < 4:  # 2 and 3
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Every prime above 3 has the form 6k - 1 or 6k + 1, so only those
    # candidate divisors up to the integer square root need testing.
    limit = isqrt(n)
    divisor = 5
    while divisor <= limit:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6
    return True
