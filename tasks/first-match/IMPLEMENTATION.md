# first-match — implementation notes

`first_match(items, target)` returns the first zero-based index whose
element equals `target`, or `None` when absent.

Validation follows the task contract, in this order:
1. Exact built-in types first: `items` must be exactly `list`,
   `target` exactly `str`, and every element exactly `str`. Bool and
   all subclasses (including nested element values) raise `TypeError`.
2. Bounds second: at most 1000 elements, and every string (elements
   and target) at most 64 Unicode code points; violations raise
   `ValueError`.

Matching is literal string equality — no trimming, normalization, or
case folding — and the input list is only read, never mutated.
Verified locally with the public checker (`check.py` → PASS) plus a
self-check mirroring the contract's type/bounds probes.
