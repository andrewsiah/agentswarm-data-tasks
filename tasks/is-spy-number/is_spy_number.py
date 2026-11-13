def is_spy_number(n):
    if type(n) is not int:
        raise TypeError("n must be an exact built-in int")
    if n < 0 or n > 10**18:
        raise ValueError("n must be in [0, 10**18]")
    digit_sum = 0
    digit_product = 1
    m = n
    while True:
        d = m % 10
        digit_sum += d
        digit_product *= d
        m //= 10
        if m == 0:
            break
    return digit_sum == digit_product
