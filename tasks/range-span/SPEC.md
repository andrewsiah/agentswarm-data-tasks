# Span between the largest and smallest integer

Implement export function rangeSpan(values) in range_span.mjs, Node 22
standard library only.

values must be a dense normal Array: prototype exactly Array.prototype, not a
Proxy (use types.isProxy from node:util; this includes revoked proxies), and
every index an own property. Reject subclasses, altered prototypes, nonarrays
and holes with exact TypeError. Every element must be a primitive number;
boxed Number objects (also subclasses), bigints, strings and all other values
raise exact TypeError. Validate ALL types before any value check. Then an
empty array raises exact RangeError, and every element must be an integer
(Number.isInteger) with absolute value at most 1e15, otherwise exact
RangeError (this rejects NaN, Infinity and fractions).

Return, as a primitive number, the largest element minus the smallest element
(0 for a one-element array). Never return -0: rangeSpan([-0]) is 0. Order
does not matter and duplicates are allowed.

Error messages are unconstrained. Never change input values or properties;
frozen arrays are supported. Ignore extra named array properties and never call
user-shadowed array methods or the input's iterator (use index loops). Index
properties are ordinary data properties. Independent calls return independent
results.

Examples (arguments -> result); every one is checked:
- `([5]) -> 0`
- `([1, 9]) -> 8`
- `([9, 1]) -> 8`
- `([3, -2, 7]) -> 9`
- `([-5, -5]) -> 0`
- `([0, 10, 5]) -> 10`
- `([-1000000000000000, 1000000000000000]) -> 2000000000000000`
- `([4, 4, 2, 8]) -> 6`
- `([-0]) -> 0`
- `([1e15,-1e15,0]) -> 2e15`
- `([]) -> RangeError`
- `([1.5]) -> RangeError`
- `([NaN]) -> RangeError`
- `([Infinity]) -> RangeError`
- `([1e15+1]) -> RangeError`
- `(['1']) -> TypeError`
- `([1n]) -> TypeError`
- `([new Number(1)]) -> TypeError`
- `([1.5,'x']) -> TypeError`
- `(Array(1)) -> TypeError`
- `(new Proxy([1],{})) -> TypeError`

Only edit range_span.mjs and optional IMPLEMENTATION.md in this task directory.
Quick run from the repository root (Node 22):
`node tasks/range-span/check.mjs --solution "$PWD/tasks/range-span/range_span.mjs"`
The issue supplies a separate trusted checker pin and offline Docker command.
A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
