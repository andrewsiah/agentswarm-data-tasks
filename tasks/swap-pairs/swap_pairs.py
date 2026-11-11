def swap_pairs(values):
    if type(values) is not list:
        raise TypeError("values must be an exact built-in list")
    for item in values:
        if type(item) is not str:
            raise TypeError("every element must be an exact built-in str")
    if len(values) > 1000:
        raise ValueError("values must contain at most 1000 elements")
    for item in values:
        if len(item) > 64:
            raise ValueError("each string must be at most 64 code points")
    result = list(values)
    for i in range(0, len(result) - 1, 2):
        result[i], result[i + 1] = result[i + 1], result[i]
    return result
