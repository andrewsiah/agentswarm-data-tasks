# matrix-transpose
Implement `matrix_transpose` in `matrix_transpose.py`. Python 3.11+ standard library only.

Fix the seeded implementation. Require rows, an exact built-in list of at most 100 rows; each row is an exact built-in list of at most 100 exact built-in ints, each in [-1000000000,1000000000]. Every row must have the same length as rows[0]; a ragged matrix raises exact ValueError. Return a fresh exact built-in list of fresh exact built-in lists that is the transpose: result[j][i] == rows[i][j], so an R x C matrix becomes C x R. The empty matrix [] returns [] (never None), and rows with zero columns, such as [[], []], also return [].

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[]]` -> `[]`
- `[[[]]]` -> `[]`
- `[[[], []]]` -> `[]`
- `[[[1]]]` -> `[[1]]`
- `[[[1, 2, 3]]]` -> `[[1], [2], [3]]`
- `[[[1], [2], [3]]]` -> `[[1, 2, 3]]`
- `[[[1, 2], [3, 4]]]` -> `[[1, 3], [2, 4]]`
- `[[[1, 2, 3], [4, 5, 6]]]` -> `[[1, 4], [2, 5], [3, 6]]`
- `[[[-1, 0], [0, -1], [5, 5]]]` -> `[[-1, 0, 5], [0, -1, 5]]`
- `[[[7, 7], [7, 7]]]` -> `[[7, 7], [7, 7]]`
- `[[[1, True]]]` -> `raises TypeError`
- `[[None]]` -> `raises TypeError`
- `[[[1, 2], [3]]]` -> `raises ValueError`
- `[[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]]` -> `raises ValueError`

Only edit `matrix_transpose.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/matrix-transpose/check.py --solution "$PWD/tasks/matrix-transpose/matrix_transpose.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
