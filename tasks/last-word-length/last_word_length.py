def last_word_length(text):
    """Return the number of code points in the last word of text.

    text must be an exact built-in str of at most 1000 Unicode code
    points. Words are maximal runs of non-whitespace characters using
    str.split() whitespace semantics, so trailing whitespace is
    ignored and empty or whitespace-only text returns 0.
    """
    if type(text) is not str:
        raise TypeError("text must be an exact built-in str")
    if len(text) > 1000:
        raise ValueError("text must be at most 1000 code points")
    words = text.split()
    if not words:
        return 0
    return len(words[-1])
