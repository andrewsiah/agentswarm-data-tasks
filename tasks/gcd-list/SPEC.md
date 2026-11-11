# gcd-list
Implement `gcd_list` in `gcd_list.py`. Python 3.11+ standard library only.

Require a NONEMPTY exact built-in list of at most 1000 exact built-in ints, each in [-1000000000000,1000000000000]; an empty list raises exact ValueError. Return the greatest common divisor of all values as a NON-NEGATIVE exact built-in int. Signs are ignored, zeros are allowed (gcd(0, x) is abs(x)) and a list of only zeros returns 0.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[12]]` -> `12`
- `[[-12]]` -> `12`
- `[[12, 18]]` -> `6`
- `[[7, 13]]` -> `1`
- `[[0, 5]]` -> `5`
- `[[0, 0]]` -> `0`
- `[[-4, 6, -10]]` -> `2`
- `[[1000000000000, 500000000000]]` -> `500000000000`
- `[[]]` -> `raises ValueError`
- `[[True]]` -> `raises TypeError`

Only edit `gcd_list.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/gcd-list/check.py --solution "$PWD/tasks/gcd-list/gcd_list.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
