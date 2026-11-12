def replace_value(items, old, new):
    """Return a new list with every element equal to old replaced by new.

    items must be an exact built-in list of exact built-in ints and old
    and new exact built-in ints, each in [-10**9, 10**9], with at most
    1000 items. The input list is never changed and the result is
    always a fresh list, even when nothing is replaced.
    """
    if type(items) is not list:
        raise TypeError("items must be an exact built-in list")
    if type(old) is not int:
        raise TypeError("old must be an exact built-in int")
    if type(new) is not int:
        raise TypeError("new must be an exact built-in int")
    for element in items:
        if type(element) is not int:
            raise TypeError("items must contain only exact built-in ints")
    if len(items) > 1000:
        raise ValueError("items must contain at most 1000 elements")
    if old < -(10**9) or old > 10**9:
        raise ValueError("old must be in [-10**9, 10**9]")
    if new < -(10**9) or new > 10**9:
        raise ValueError("new must be in [-10**9, 10**9]")
    for element in items:
        if element < -(10**9) or element > 10**9:
            raise ValueError("items elements must be in [-10**9, 10**9]")
    return [new if element == old else element for element in items]
