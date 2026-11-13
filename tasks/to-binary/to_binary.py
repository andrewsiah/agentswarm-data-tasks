def to_binary(n):
    if type(n) is not int:
        raise TypeError("n must be an exact int")
    if n < 0 or n > 2**64 - 1:
        raise ValueError("n must be in [0, 2**64 - 1]")
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append("1" if n % 2 else "0")
        n //= 2
    digits.reverse()
    return "".join(digits)
