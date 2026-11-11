def trim_zeros(values):
    if not isinstance(values, list):
        raise TypeError()
    start=0
    while start<len(values) and values[start]==0:
        start+=1
    return values[start:]
