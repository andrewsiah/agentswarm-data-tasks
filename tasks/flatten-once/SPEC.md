# flatten-once
Implement `flatten_once` in `flatten_once.py`. Python 3.11+ standard library only.

Require values, an exact built-in list of at most 100 exact built-in lists, each holding at most 100 exact built-in ints in [-1000000000,1000000000]. Return a fresh exact built-in list with the ints of every inner list, in outer order and then inner order. Flatten exactly one level: deeper nesting is a wrong type. Do not sort, reverse or remove duplicates; empty inner lists contribute nothing.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[]]` -> `[]`
- `[[[]]]` -> `[]`
- `[[[1], [2, 3]]]` -> `[1, 2, 3]`
- `[[[3, 1], [], [2]]]` -> `[3, 1, 2]`
- `[[[1, 1], [1]]]` -> `[1, 1, 1]`
- `[[[-1], [0], [1]]]` -> `[-1, 0, 1]`
- `[[[5, 4], [3, 2]]]` -> `[5, 4, 3, 2]`
- `[[[1000000000], [-1000000000]]]` -> `[1000000000, -1000000000]`
- `[[[1, [2]]]]` -> `raises TypeError`
- `[[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]]` -> `raises ValueError`

Only edit `flatten_once.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/flatten-once/check.py --solution "$PWD/tasks/flatten-once/flatten_once.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
