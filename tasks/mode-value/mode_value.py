def mode_value(values):
    if type(values) is not list:
        raise TypeError("values must be an exact built-in list")
    for v in values:
        if type(v) is not int:
            raise TypeError("each value must be an exact built-in int")
    if len(values) == 0:
        raise ValueError("values must be nonempty")
    if len(values) > 1000:
        raise ValueError("values must contain at most 1000 items")
    for v in values:
        if v < -1000000000 or v > 1000000000:
            raise ValueError("each value must be in [-1000000000, 1000000000]")
    counts = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1
    best = None
    best_count = -1
    for v, c in counts.items():
        if c > best_count or (c == best_count and v < best):
            best = v
            best_count = c
    return best
