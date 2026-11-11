def second_largest(values):
    if type(values) is not list:
        raise TypeError("values must be an exact built-in list")
    for item in values:
        if type(item) is not int:
            raise TypeError("every element must be an exact built-in int")
    if len(values) > 1000:
        raise ValueError("values must contain at most 1000 elements")
    for item in values:
        if item < -1000000000 or item > 1000000000:
            raise ValueError("each int must be in [-1000000000, 1000000000]")
    distinct = set(values)
    if len(distinct) < 2:
        raise ValueError("values must contain at least two distinct values")
    distinct.discard(max(distinct))
    return max(distinct)
