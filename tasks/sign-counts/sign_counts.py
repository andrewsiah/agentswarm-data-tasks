def sign_counts(values):
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
    negative = 0
    zero = 0
    positive = 0
    for v in values:
        if v < 0:
            negative += 1
        elif v == 0:
            zero += 1
        else:
            positive += 1
    return {"negative": negative, "zero": zero, "positive": positive}
