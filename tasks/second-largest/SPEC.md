# second-largest
Implement `second_largest` in `second_largest.py`. Python 3.11+ standard library only.

Require an exact built-in list of at most 1000 exact built-in ints, each in [-1000000000,1000000000], containing AT LEAST TWO DISTINCT values; otherwise (including the empty list and lists such as [7,7]) raise exact ValueError. Return, as an exact built-in int, the largest value that is strictly smaller than the maximum. Duplicates of the maximum do not count: second_largest([9,9,8]) is 8.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[1, 2]]` -> `1`
- `[[5, 3, 9, 7]]` -> `7`
- `[[9, 9, 8]]` -> `8`
- `[[2, 2, 3, 3]]` -> `2`
- `[[-1, -2, -3]]` -> `-2`
- `[[0, -5]]` -> `-5`
- `[[1000000000, -1000000000]]` -> `-1000000000`
- `[[4, 1, 4, 1, 4]]` -> `1`
- `[[7, 7]]` -> `raises ValueError`
- `[[True, 2]]` -> `raises TypeError`

Only edit `second_largest.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/second-largest/check.py --solution "$PWD/tasks/second-largest/second_largest.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
