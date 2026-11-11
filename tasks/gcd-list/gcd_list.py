from math import gcd


def gcd_list(values):
    if type(values) is not list:
        raise TypeError("values must be an exact built-in list")
    for item in values:
        if type(item) is not int:
            raise TypeError("every element must be an exact built-in int")
    if len(values) == 0:
        raise ValueError("values must be nonempty")
    if len(values) > 1000:
        raise ValueError("values must contain at most 1000 elements")
    for item in values:
        if item < -1000000000000 or item > 1000000000000:
            raise ValueError("each int must be in [-1000000000000, 1000000000000]")
    result = 0
    for item in values:
        result = gcd(result, item)
    return result
