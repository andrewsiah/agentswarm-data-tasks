"""Count whitespace-separated words in a bounded string. See SPEC.md.

text must be an exact built-in str of at most 1000 Unicode code points;
str subclasses and every other type raise TypeError, and an over-long
string raises ValueError (types are validated before lengths). A word is
a maximal run of non-whitespace characters, where whitespace is exactly
what str.split() with no arguments splits on. Returns an exact built-in
int. No input mutation, retained state or I/O.
"""

_MAX_CODE_POINTS = 1000


def count_words(text):
    if type(text) is not str:
        raise TypeError("text must be an exact built-in str")
    if len(text) > _MAX_CODE_POINTS:
        raise ValueError("text longer than 1000 code points")
    return len(text.split())
