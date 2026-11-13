MAX_ITEMS = 1000
LIMIT = 10**9


def remove_at(items, index):
    # Phase 1: validate every type first (exact built-ins only, so bool and
    # subclasses of int/list are rejected, including nested elements).
    if type(items) is not list:
        raise TypeError("items must be a list")
    for value in items:
        if type(value) is not int:
            raise TypeError("items must contain only ints")
    if type(index) is not int:
        raise TypeError("index must be an int")

    # Phase 2: lengths and ranges.
    if len(items) > MAX_ITEMS:
        raise ValueError("too many items")
    for value in items:
        if value < -LIMIT or value > LIMIT:
            raise ValueError("item out of range")
    if index < 0 or index >= len(items):
        raise ValueError("index out of range")

    # Slicing an exact list builds a new exact list; items is never touched.
    return items[:index] + items[index + 1:]
