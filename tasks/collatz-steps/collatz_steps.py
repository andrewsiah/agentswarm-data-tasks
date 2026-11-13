def collatz_steps(n):
    if type(n) is not int:
        raise TypeError("n must be an exact int")
    if n < 1 or n > 10**12:
        raise ValueError("n must be in [1, 10**12]")
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps
