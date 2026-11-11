_VOWELS = frozenset("aeiouAEIOU")


def vowel_count(text):
    if type(text) is not str:
        raise TypeError("text must be an exact built-in str")
    if len(text) > 1000:
        raise ValueError("text must be at most 1000 Unicode code points")
    return sum(1 for ch in text if ch in _VOWELS)
