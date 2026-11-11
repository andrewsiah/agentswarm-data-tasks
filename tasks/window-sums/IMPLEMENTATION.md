# Implementation notes: window_sums -> contiguous window sums

## Approach
- Validate **all** types first (`type(x) is ...`), so a wrongly typed argument
  raises `TypeError` even when another argument is out of range (type precedence
  per SPEC): the list itself, the `size`, and every element. `type(True) is
  bool`, so `bool` and every subclass of `int` or `list` is rejected, nested
  values included.
- Range-validate afterwards with `ValueError`: at most 1000 elements, every
  element in `[-1000000000, 1000000000]`, and `size` in `[1, 1000]`.
- A window is exactly `size` elements long, so `size > len(values)` means there
  is no complete window: the result is a fresh empty list, never a partial
  window.
- The sums come from one running total: the first window is summed, and each
  following window adds the element that enters and subtracts the one that
  leaves. The result has `len(values) - size + 1` entries, the last window
  included.
- A fresh list is built on every call, the input is never mutated, nothing is
  retained between calls, and the module is stdlib only and self-contained.

## Result
`PASS window-sums: 14 examples plus exact types, bounds and isolation probes`

The same probes against the seeded implementation fail 24 times: seven spec
examples (every one of them short by the last window), thirteen type probes
(`bool`, `int` and `list` subclasses, `float`, `str`, `None`, a `bool` nested
in a list of 1002 elements) and four bound probes (a `size` of 0, -1 or 1001,
and an element outside the value range).
