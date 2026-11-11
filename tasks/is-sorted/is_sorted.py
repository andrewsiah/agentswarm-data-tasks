def is_sorted(values):
    if type(values) is not list:
        raise TypeError("values must be a list")
    if any(type(value) is not int for value in values):
        raise TypeError("every value must be an int")
    if len(values) > 1000:
        raise ValueError("values must contain at most 1000 items")
    if any(value < -1000000000 or value > 1000000000 for value in values):
        raise ValueError("every value must be in [-1000000000, 1000000000]")
    return all(values[index] <= values[index + 1] for index in range(len(values) - 1))
