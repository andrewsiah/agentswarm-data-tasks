# power-of-two
Implement `power_of_two` in `power_of_two.py`. Python 3.11+ standard library only.

Require n, an exact built-in int in [-1000000000000000000,1000000000000000000]. Return the exact bool True when n equals 2**k for some integer k >= 0 (so 1, 2, 4, 8 and so on), otherwise the exact bool False. Zero and every negative number return False.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[1]` -> `True`
- `[2]` -> `True`
- `[3]` -> `False`
- `[0]` -> `False`
- `[-2]` -> `False`
- `[64]` -> `True`
- `[96]` -> `False`
- `[1024]` -> `True`
- `[576460752303423488]` -> `True`
- `[-1]` -> `False`
- `[True]` -> `raises TypeError`
- `[1152921504606846976]` -> `raises ValueError`

Only edit `power_of_two.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/power-of-two/check.py --solution "$PWD/tasks/power-of-two/power_of_two.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
