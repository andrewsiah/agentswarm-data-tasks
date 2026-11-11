# is-sorted
Implement `is_sorted` in `is_sorted.py`. Python 3.11+ standard library only.

Require an exact built-in list of at most 1000 exact built-in ints, each in [-1000000000,1000000000]. Return the exact bool True when every element is less than or equal to the element after it (non-decreasing order; equal neighbours are allowed), otherwise the exact bool False. The empty list and one-element lists return True. Compare signed values, not absolute values.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[]]` -> `True`
- `[[5]]` -> `True`
- `[[1, 2, 3]]` -> `True`
- `[[1, 1, 2]]` -> `True`
- `[[3, 2]]` -> `False`
- `[[1, 3, 2]]` -> `False`
- `[[-5, -1, 0]]` -> `True`
- `[[0, -1]]` -> `False`
- `[[2, 2, 2]]` -> `True`
- `[[1, 2, 3, 0]]` -> `False`
- `[[True, 1]]` -> `raises TypeError`
- `[[1000000001]]` -> `raises ValueError`

Only edit `is_sorted.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/is-sorted/check.py --solution "$PWD/tasks/is-sorted/is_sorted.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
