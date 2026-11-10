MAX_VALUES = 1000
MIN_VALUE = -1000000000
MAX_VALUE = 1000000000
MIN_SIZE = 1
MAX_SIZE = 1000


def window_sums(values, size):
    """Return the sum of every contiguous window of exactly size elements."""
    if type(values) is not list:
        raise TypeError("values must be a built-in list")
    if type(size) is not int:
        raise TypeError("size must be a built-in int")
    for value in values:
        if type(value) is not int:
            raise TypeError("values must contain exact built-in ints")

    if len(values) > MAX_VALUES:
        raise ValueError("values must contain at most 1000 elements")
    for value in values:
        if value < MIN_VALUE or value > MAX_VALUE:
            raise ValueError("elements must be in [-1000000000, 1000000000]")
    if size < MIN_SIZE or size > MAX_SIZE:
        raise ValueError("size must be in [1, 1000]")

    if size > len(values):
        return []

    totals = []
    total = sum(values[:size])
    totals.append(total)
    for index in range(size, len(values)):
        total += values[index] - values[index - size]
        totals.append(total)
    return totals
