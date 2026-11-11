# swap-pairs
Implement `swap_pairs` in `swap_pairs.py`. Python 3.11+ standard library only.

Require an exact built-in list of at most 1000 exact built-in strs, each of at most 64 Unicode code points. Return a fresh exact built-in list in which elements 0 and 1 swap places, then elements 2 and 3, and so on. For an odd length the last element stays at the end. Do not reverse, rotate or sort; strings are opaque (no trimming or normalization).

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[]]` -> `[]`
- `[['a']]` -> `['a']`
- `[['a', 'b']]` -> `['b', 'a']`
- `[['a', 'b', 'c']]` -> `['b', 'a', 'c']`
- `[['a', 'b', 'c', 'd']]` -> `['b', 'a', 'd', 'c']`
- `[['x', 'x', 'y']]` -> `['x', 'x', 'y']`
- `[['', 'é']]` -> `['é', '']`
- `[['1', '2', '3', '4', '5']]` -> `['2', '1', '4', '3', '5']`
- `[[1, 'a']]` -> `raises TypeError`
- `[['xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx']]` -> `raises ValueError`

Only edit `swap_pairs.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/swap-pairs/check.py --solution "$PWD/tasks/swap-pairs/swap_pairs.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
