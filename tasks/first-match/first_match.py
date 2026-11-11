"""first_match(items, target): first index whose element equals target.

Contract:
- items is an exact built-in list of at most 1000 exact built-in
  strings, each at most 64 Unicode code points; target is an exact
  built-in string of at most 64 code points.
- Returns the first matching zero-based index as an exact int, or
  None if absent. Equality is literal: no trimming, normalization
  or case folding.
- Bool and all subclasses (including elements) are rejected with
  TypeError. ALL types are validated first; bounds violations then
  raise ValueError.
- The input list is never mutated.
"""


def first_match(items, target):
    if type(items) is not list:
        raise TypeError("items must be an exact built-in list")
    if type(target) is not str:
        raise TypeError("target must be an exact built-in string")
    for element in items:
        if type(element) is not str:
            raise TypeError("every element must be an exact built-in string")
    if len(items) > 1000:
        raise ValueError("items must contain at most 1000 elements")
    if len(target) > 64:
        raise ValueError("target must be at most 64 code points")
    for element in items:
        if len(element) > 64:
            raise ValueError("every element must be at most 64 code points")
    for index, element in enumerate(items):
        if element == target:
            return index
    return None
