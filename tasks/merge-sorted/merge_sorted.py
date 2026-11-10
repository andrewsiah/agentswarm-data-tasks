_MAX_PER_LIST = 1000
_MIN_VALUE = -1000000000
_MAX_VALUE = 1000000000


def merge_sorted(left, right):
    if type(left) is not list or type(right) is not list:
        raise TypeError("merge_sorted requires two built-in lists")
    for values in (left, right):
        for value in values:
            if type(value) is not int:
                raise TypeError("merge_sorted requires built-in int elements")
    for values in (left, right):
        if len(values) > _MAX_PER_LIST:
            raise ValueError("each input list must contain at most 1000 elements")
        for value in values:
            if value < _MIN_VALUE or value > _MAX_VALUE:
                raise ValueError("elements must be in [-1000000000, 1000000000]")
        for index in range(len(values) - 1):
            if values[index] > values[index + 1]:
                raise ValueError("each input list must be sorted nondecreasing")
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out
