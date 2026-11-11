def trim_zeros(values):
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
    start = 0
    end = len(values)
    while start < end and values[start] == 0:
        start += 1
    while end > start and values[end - 1] == 0:
        end -= 1
    return list(values[start:end])
