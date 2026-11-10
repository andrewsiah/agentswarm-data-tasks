MAX_ITEMS = 1000
MAX_STRING_LENGTH = 64
MIN_STEP = 1
MAX_STEP = 1000


def take_every(items, step):
    if type(items) is not list:
        raise TypeError("items must be a list")
    for item in items:
        if type(item) is not str:
            raise TypeError("items must contain only strings")
    if type(step) is not int:
        raise TypeError("step must be an int")

    if len(items) > MAX_ITEMS:
        raise ValueError("items must contain at most 1000 strings")
    for item in items:
        if len(item) > MAX_STRING_LENGTH:
            raise ValueError("each string must be at most 64 code points")
    if not MIN_STEP <= step <= MAX_STEP:
        raise ValueError("step must be between 1 and 1000")

    return items[::step]
