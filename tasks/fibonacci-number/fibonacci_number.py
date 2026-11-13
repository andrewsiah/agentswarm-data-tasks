def fibonacci_number(n):
    if type(n) is not int:
        raise TypeError("n must be an exact int")
    if n < 0 or n > 1000:
        raise ValueError("n must be in [0, 1000]")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
