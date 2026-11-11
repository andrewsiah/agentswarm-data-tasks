def clamp_score(value, low, high):
    for x in (value, low, high):
        if type(x) is not int:
            raise TypeError("value, low and high must be exact built-in ints")
    for x in (value, low, high):
        if x < -1000000000 or x > 1000000000:
            raise ValueError("value, low and high must be in [-1000000000, 1000000000]")
    if low > high:
        raise ValueError("low must be <= high")
    if value < low:
        return low
    if value > high:
        return high
    return value
