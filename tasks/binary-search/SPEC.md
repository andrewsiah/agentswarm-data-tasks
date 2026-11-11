# binary-search
Implement `binary_search` in `binary_search.py`. Python 3.11+ standard library only.

Fix the seeded implementation. Require values, an exact built-in list of at most 1000 exact built-in ints, each in [-1000000000,1000000000], in STRICTLY increasing order (duplicates or any decrease raise exact ValueError), and target, an exact built-in int of any size. Return, as an exact built-in int, the index of target in values, or -1 (never None) when target is absent. The empty list returns -1.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[], 5]` -> `-1`
- `[[5], 5]` -> `0`
- `[[5], 4]` -> `-1`
- `[[1, 3, 5, 7], 7]` -> `3`
- `[[1, 3, 5, 7], 1]` -> `0`
- `[[1, 3, 5, 7], 4]` -> `-1`
- `[[-10, -3, 0, 8], -3]` -> `1`
- `[[1, 3, 5, 7], 8]` -> `-1`
- `[[2, 4], 100000000000000000000]` -> `-1`
- `[[1, 2], True]` -> `raises TypeError`
- `[[2, 1], 1]` -> `raises ValueError`
- `[[1, 1], 1]` -> `raises ValueError`

Only edit `binary_search.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/binary-search/check.py --solution "$PWD/tasks/binary-search/binary_search.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
