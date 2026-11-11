def popcount(n):
    if type(n) is not int:
         raise TypeError("Input must be a non negative integer")
    if n<0 or n>10**18:
         raise ValueError("Input must be between 0 and 10**30")
    return n.bit_count()
    