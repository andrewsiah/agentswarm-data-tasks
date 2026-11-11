def pairwise_diffs(values):
    if type(values) is not list:
        raise TypeError("values must be an exact built-in list")
    for v in values:
        if type(v) is not int:
            raise TypeError("each value must be an exact built-in int")
    if len(values) > 1000:
        raise ValueError("values must contain at most 1000 items")
    for v in values:
        if v < -1000000000 or v > 1000000000:
            raise ValueError("each value must be in [-1000000000, 1000000000]")
    result = []
    for i in range(len(values) - 1):
        result.append(values[i + 1] - values[i])
    return result
