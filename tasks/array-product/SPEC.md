# Product of integers with a safe-integer guard

Implement export function arrayProduct(values) in array_product.mjs, Node 22
standard library only.

values must be a dense normal Array: prototype exactly Array.prototype, not a
Proxy (use types.isProxy from node:util; this includes revoked proxies), and
every index an own property. Reject subclasses, altered prototypes, nonarrays
and holes with exact TypeError. Every element must be a primitive number;
boxed Number objects (also subclasses), bigints, strings and all other values
raise exact TypeError. Validate ALL types before any value check. Then every
element must be an integer (Number.isInteger) with absolute value at most 1e9,
otherwise exact RangeError (this rejects NaN, Infinity and fractions).

Return, as a primitive number, the exact mathematical product of all
elements. The empty array returns 1. When the absolute value of the exact
product is greater than Number.MAX_SAFE_INTEGER (2**53 - 1), throw exact
RangeError. Only the final product counts: [1e9, 1e9, 0] returns 0. Never
return -0: arrayProduct([0, -5]) is 0.

Error messages are unconstrained. Never change input values or properties;
frozen arrays are supported. Ignore extra named array properties and never call
user-shadowed array methods or the input's iterator (use index loops). Index
properties are ordinary data properties. Independent calls return independent
results.

Examples (arguments -> result); every one is checked:
- `([]) -> 1`
- `([5]) -> 5`
- `([2, 3, 4]) -> 24`
- `([-2, 3]) -> -6`
- `([-2, -3]) -> 6`
- `([7, 0, 9]) -> 0`
- `([1, 1, 1]) -> 1`
- `([6361, 69431, 20394401]) -> 9007199254740991`
- `([-1000000000, 1000000]) -> -1000000000000000`
- `([1000000000, 1000000000, 0]) -> 0`
- `([0,-5]) -> 0`
- `([-0]) -> 0`
- `([-5,0]) -> 0`
- `([2**26,2**26]) -> 2**52`
- `([2**26,2**27]) -> RangeError`
- `([-(2**26),2**27]) -> RangeError`
- `([1.5]) -> RangeError`
- `([NaN]) -> RangeError`
- `([Infinity]) -> RangeError`
- `([1e9+1]) -> RangeError`
- `(['1']) -> TypeError`
- `([1n]) -> TypeError`
- `([new Number(1)]) -> TypeError`
- `([1.5,'x']) -> TypeError`
- `(Array(1)) -> TypeError`
- `(new Proxy([1],{})) -> TypeError`

Only edit array_product.mjs and optional IMPLEMENTATION.md in this task directory.
Quick run from the repository root (Node 22):
`node tasks/array-product/check.mjs --solution "$PWD/tasks/array-product/array_product.mjs"`
The issue supplies a separate trusted checker pin and offline Docker command.
A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
