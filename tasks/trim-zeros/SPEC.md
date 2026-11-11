# trim-zeros
Implement `trim_zeros` in `trim_zeros.py`. Python 3.11+ standard library only.

Fix the seeded implementation. Require an exact built-in list of at most 1000 exact built-in ints, each in [-1000000000,1000000000]. Return a fresh exact built-in list with every LEADING and every TRAILING 0 removed; zeros between nonzero values stay in place and the order is kept. A list of only zeros (and the empty list) returns a fresh []. False is a bool, not the int 0, and raises exact TypeError.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[]]` -> `[]`
- `[[0, 0]]` -> `[]`
- `[[0, 1, 0]]` -> `[1]`
- `[[0, 0, 3, 0, 4, 0, 0]]` -> `[3, 0, 4]`
- `[[5]]` -> `[5]`
- `[[1, 0, 0, 2]]` -> `[1, 0, 0, 2]`
- `[[-1, 0]]` -> `[-1]`
- `[[0, 1000000000, -1000000000, 0]]` -> `[1000000000, -1000000000]`
- `[[False, 1]]` -> `raises TypeError`
- `[[1000000001]]` -> `raises ValueError`

Only edit `trim_zeros.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/trim-zeros/check.py --solution "$PWD/tasks/trim-zeros/trim_zeros.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
