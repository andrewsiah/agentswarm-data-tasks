# popcount
Implement `popcount` in `popcount.py`. Python 3.11+ standard library only.

Require n, an exact built-in int in [0,1000000000000000000]; negative numbers raise exact ValueError. Return, as an exact built-in int, how many 1 bits the binary representation of n has (so 0 -> 0, 7 -> 3, 8 -> 1). Do not count 0 bits, the bit length or the parity.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[0]` -> `0`
- `[1]` -> `1`
- `[2]` -> `1`
- `[3]` -> `2`
- `[7]` -> `3`
- `[8]` -> `1`
- `[255]` -> `8`
- `[256]` -> `1`
- `[1023]` -> `10`
- `[576460752303423488]` -> `1`
- `[576460752303423487]` -> `59`
- `[1000000000000000000]` -> `24`
- `[True]` -> `raises TypeError`
- `[4.0]` -> `raises TypeError`
- `[-1]` -> `raises ValueError`
- `[1000000000000000001]` -> `raises ValueError`

Only edit `popcount.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/popcount/check.py --solution "$PWD/tasks/popcount/popcount.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
