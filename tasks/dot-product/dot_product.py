def dot_product(a, b):
    if type(a) is not list or type(b) is not list:
        raise TypeError("both arguments must be exact lists")

    for x in a:
        if type(x) is not int:
            raise TypeError("elements of a must be exact integers")

    for y in b:
        if type(y) is not int:
            raise TypeError("elements of b must be exact integers")

    if len(a) != len(b):
        raise ValueError("lists must have equal length")

    if len(a) > 1000:
        raise ValueError("list length exceeds 1000")

    total = 0
    for x, y in zip(a, b):
        if not (-1000000000 <= x <= 1000000000):
            raise ValueError(f"integer {x} out of range [-1000000000, 1000000000]")
        if not (-1000000000 <= y <= 1000000000):
            raise ValueError(f"integer {y} out of range [-1000000000, 1000000000]")
        total += x * y

    return total
