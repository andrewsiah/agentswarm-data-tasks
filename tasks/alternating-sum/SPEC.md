# alternating-sum
Implement `alternating_sum` in `alternating_sum.py`. Python 3.11+ standard library only.

Require values, an exact built-in list of at most 1000 exact built-in ints, each in [-1000000000,1000000000]. Return, as an exact built-in int, values[0] - values[1] + values[2] - values[3] + ... : elements at even indexes (0, 2, 4, ...) are added and elements at odd indexes are subtracted, using their signed values. The empty list returns 0.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[]]` -> `0`
- `[[5]]` -> `5`
- `[[5, 3]]` -> `2`
- `[[1, 2, 3]]` -> `2`
- `[[1, 2, 3, 4]]` -> `-2`
- `[[-5, 3]]` -> `-8`
- `[[0, -4]]` -> `4`
- `[[10, 10, 10, 10]]` -> `0`
- `[[-1, -1, -1]]` -> `-1`
- `[[7, 0, 0, 0, 7]]` -> `14`
- `[[True, 1]]` -> `raises TypeError`
- `[[1000000001]]` -> `raises ValueError`

Only edit `alternating_sum.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/alternating-sum/check.py --solution "$PWD/tasks/alternating-sum/alternating_sum.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
