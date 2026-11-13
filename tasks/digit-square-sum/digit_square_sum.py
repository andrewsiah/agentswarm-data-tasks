def digit_square_sum(n: int) -> int:
    # Check exact built-in int type first (rejects bool and int subclasses)
    if type(n) is not int:
        raise TypeError("n must be an exact built-in int")
    
    # Check range [0, 10**18]
    if n < 0 or n > 10**18:
        raise ValueError("n must be between 0 and 10**18 inclusive")
    
    # Convert to string, square each digit, and return the sum
    return sum(int(digit) ** 2 for digit in str(n))