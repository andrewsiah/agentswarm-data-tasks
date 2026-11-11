"""Alternating sum of a bounded integer list. See SPEC.md.

values must be an exact built-in list of at most 1000 exact built-in ints,
each in [-1000000000, 1000000000]. Bool and all subclasses of the required
builtins raise TypeError, as does any other wrong type; all types are
validated before lengths/ranges, which raise ValueError. Returns, as an
exact built-in int, values[0] - values[1] + values[2] - ... ; the empty
list returns 0. No input mutation, no retained state, no I/O.
"""

_MAX_LENGTH = 1000
_MIN_VALUE = -1000000000
_MAX_VALUE = 1000000000


def alternating_sum(values):
    if type(values) is not list:
        raise TypeError("values must be an exact built-in list")
    for value in values:
        if type(value) is not int:
            raise TypeError("each value must be an exact built-in int")
    if len(values) > _MAX_LENGTH:
        raise ValueError("at most 1000 values")
    for value in values:
        if value < _MIN_VALUE or value > _MAX_VALUE:
            raise ValueError("value out of range")
    total = 0
    for index, value in enumerate(values):
        if index % 2 == 0:
            total += value
        else:
            total -= value
    return total
