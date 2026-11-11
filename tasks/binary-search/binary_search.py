def binary_search(values, target):
    if type(values) is not list:
        raise TypeError("values must be a list")
    if type(target) is not int:
        raise TypeError("target must be an int")

    for value in values:
        if type(value) is not int:
            raise TypeError("all values must be ints")

    if len(values) > 1000:
        raise ValueError("values must contain at most 1000 items")

    for value in values:
        if value < -1000000000 or value > 1000000000:
            raise ValueError("all values must be in [-1000000000, 1000000000]")

    for previous, current in zip(values, values[1:]):
        if previous >= current:
            raise ValueError("values must be strictly increasing")

    left = 0
    right = len(values)
    while left < right:
        middle = (left + right) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle
    return -1
