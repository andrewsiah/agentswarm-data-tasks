"""Happy number check using exact integer arithmetic."""

_MAX_N = 10**18


def _digit_square_sum(n: int) -> int:
    total = 0
    while n:
        n, d = divmod(n, 10)
        total += d * d
    return total


def is_happy(n: int) -> bool:
    """Return True iff repeatedly replacing n by the sum of the squares of
    its decimal digits reaches 1; False if a value repeats first.

    n must be an exact built-in int in [1, 10**18]. bool, int subclasses
    and all other types raise TypeError; out-of-range values raise
    ValueError (type is validated before range).
    """
    # `type(n) is not int` rejects bool, int subclasses and every other type.
    if type(n) is not int:
        raise TypeError("n must be an exact built-in int")
    if n < 1 or n > _MAX_N:
        raise ValueError("n must be in the range [1, 10**18]")

    seen = set()  # local only, discarded on return
    while n != 1 and n not in seen:
        seen.add(n)
        n = _digit_square_sum(n)
    return n == 1