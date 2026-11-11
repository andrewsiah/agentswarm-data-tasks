def last_match(items, target):
    if type(items) is not list:
        raise TypeError("items must be an exact built-in list")
    if type(target) is not str:
        raise TypeError("target must be an exact built-in str")
    for item in items:
        if type(item) is not str:
            raise TypeError("every element must be an exact built-in str")
    if len(items) > 1000:
        raise ValueError("items must contain at most 1000 elements")
    if len(target) > 64:
        raise ValueError("target must be at most 64 code points")
    for item in items:
        if len(item) > 64:
            raise ValueError("each string must be at most 64 code points")
    result = None
    for index, item in enumerate(items):
        if item == target:
            result = index
    return result
