"""Armstrong (narcissistic) number check using exact integer arithmetic."""

_MAX_N = 10**15


def is_armstrong(n: int) -> bool:
    """Return True iff n equals the sum of its decimal digits, each raised
    to the power of the number of digits.

    n must be an exact built-in int in [0, 10**15]. bool, int subclasses
    and all other types raise TypeError; out-of-range values raise
    ValueError (type is validated before range).
    """
    # `type(n) is not int` rejects bool, int subclasses and every other type.
    if type(n) is not int:
        raise TypeError("n must be an exact built-in int")
    if n < 0 or n > _MAX_N:
        raise ValueError("n must be in the range [0, 10**15]")

    digits = str(n)  # no leading zeros; "0" has one digit
    k = len(digits)
    return sum(int(d) ** k for d in digits) == n