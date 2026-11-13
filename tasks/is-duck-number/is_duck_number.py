def is_duck_number(n):
    if type(n) is not int:
        raise TypeError("Input must be an integer.")

    if not (0 <= n <= 10**18):
        raise ValueError("Input must be between 0 and 10^18.")

    if n == 0 or '0' not in str(n):
        return False
    return True
