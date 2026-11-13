MAX_VALUE = 10**18


def is_tidy_number(n):
    # Exact-type check first: rejects bool and int subclasses.
    if type(n) is not int:
        raise TypeError("n must be an int")
    if n < 0 or n > MAX_VALUE:
        raise ValueError("n must be in [0, 10**18]")

    # Digits of a non-negative int never have leading zeros; str(0) == "0".
    digits = str(n)
    for i in range(1, len(digits)):
        if digits[i] < digits[i - 1]:
            return False
    return True
