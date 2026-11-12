
from math import isqrt


def aliquot_sum(n):
    if type(n) is not int:
        raise TypeError("n must be an exact built-in int")

    if n < 1 or n > 10**12:
        raise ValueError("n must be between 1 and 10**12")

    if n == 1:
        return 0

    total = 1

    for divisor in range(2, isqrt(n) + 1):
        if n % divisor == 0:
            total += divisor

            paired_divisor = n // divisor

            if paired_divisor != divisor:
                total += paired_divisor

    return total
