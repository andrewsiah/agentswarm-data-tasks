"""Transpose a rectangular integer matrix.

Contract (see SPEC.md):
- ``rows`` must be an exact built-in list of at most 100 rows; each row an
  exact built-in list of at most 100 exact built-in ints, each in
  [-1000000000, 1000000000]. Bool and every subclass of a required builtin
  are rejected with TypeError, as is any other wrong type.
- All types are validated before any length or range check; length, range
  and ragged-row problems raise ValueError.
- Returns a fresh list of fresh lists: result[j][i] == rows[i][j]. The
  empty matrix and zero-column matrices return [].
"""

_MAX_DIM = 100
_MIN_VALUE = -1000000000
_MAX_VALUE = 1000000000


def matrix_transpose(rows):
    if type(rows) is not list:
        raise TypeError("rows must be an exact built-in list")
    # Validate every type before any length or range check.
    for row in rows:
        if type(row) is not list:
            raise TypeError("each row must be an exact built-in list")
        for value in row:
            if type(value) is not int:
                raise TypeError("each value must be an exact built-in int")
    # Length checks.
    if len(rows) > _MAX_DIM:
        raise ValueError("at most 100 rows")
    for row in rows:
        if len(row) > _MAX_DIM:
            raise ValueError("at most 100 columns")
    if rows:
        width = len(rows[0])
        for row in rows:
            if len(row) != width:
                raise ValueError("ragged matrix: rows differ in length")
    # Range checks.
    for row in rows:
        for value in row:
            if value < _MIN_VALUE or value > _MAX_VALUE:
                raise ValueError("value out of range")
    if not rows:
        return []
    width = len(rows[0])
    if width == 0:
        return []
    return [[rows[i][j] for i in range(len(rows))] for j in range(width)]
