def move_to_front(items, index):
    if type(items) is not list:
        raise TypeError("items must be a built-in list")

    if type(index) is not int:
        raise TypeError("index must be a built-in integer")

    for item in items:
        if type(item) is not int:
            raise TypeError("all elements must be built-in integers")

    if len(items) > 1000:
        raise ValueError("list cannot contain more than 1000 elements")

    for item in items:
        if item < -1000000000 or item > 1000000000:
            raise ValueError("element outside allowed range")

    if index < 0 or index >= len(items):
        raise ValueError("index out of range")

    return items[index:index + 1] + items[:index] + items[index + 1:]