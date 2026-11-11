# digit-sum
Implement `digit_sum` in `digit_sum.py`. Python 3.11+ standard library only.

Require n, an exact built-in int in [-1000000000000000000,1000000000000000000]. Return the sum of the decimal digits of the absolute value of n as an exact built-in int. The sign is ignored (never subtract digits or return a negative result), 0 returns 0, and this is a single digit sum, not a repeated digital root.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[0]` -> `0`
- `[7]` -> `7`
- `[123]` -> `6`
- `[-123]` -> `6`
- `[1000]` -> `1`
- `[99]` -> `18`
- `[-909]` -> `18`
- `[1000000000000000000]` -> `1`
- `[-999999999999999999]` -> `162`
- `[True]` -> `raises TypeError`
- `[1000000000000000001]` -> `raises ValueError`

Only edit `digit_sum.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/digit-sum/check.py --solution "$PWD/tasks/digit-sum/digit_sum.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
