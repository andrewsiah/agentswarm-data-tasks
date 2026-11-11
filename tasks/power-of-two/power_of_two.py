def power_of_two(n):
    if type(n) is not int:
        raise TypeError("n must be an int")
    if n < -1000000000000000000 or n > 1000000000000000000:
        raise ValueError("n is out of range")
    return n > 0 and n & (n - 1) == 0
