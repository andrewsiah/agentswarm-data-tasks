# Count strings that start with a prefix

Implement export function prefixCount(values, prefix) in prefix_count.mjs,
Node 22 standard library only.

values must be a dense normal Array: prototype exactly Array.prototype, not a
Proxy (use types.isProxy from node:util; this includes revoked proxies), and
every index an own property. Reject subclasses, altered prototypes, nonarrays
and holes with exact TypeError. Every element must be a primitive string; boxed
String objects (also subclasses) and all other values raise exact TypeError.
prefix must be a primitive string (boxed String objects raise exact TypeError).
Validate values and the type of prefix before its length, so ([1],'x'.repeat(65))
raises TypeError. Then prefix.length (UTF-16 code units) must be at most 64,
otherwise exact RangeError.

Return, as a primitive number, how many elements start with prefix. Matching is
case-sensitive and exact at the START of each string (not anywhere inside, not
at the end); no trimming or normalization. Duplicates count every time. The
empty prefix matches every element.

Error messages are unconstrained. Never change input values or properties;
frozen arrays are supported. Ignore extra named array properties and never call
user-shadowed array methods or the input's iterator (use index loops). Index
properties are ordinary data properties. Independent calls return independent
results.

Examples (arguments -> result); every one is checked:
- `([], 'a') -> 0`
- `(['apple', 'avocado', 'banana'], 'a') -> 2`
- `(['Apple', 'apple'], 'a') -> 1`
- `(['ab', 'b'], '') -> 2`
- `(['abc', 'ab', 'a'], 'ab') -> 2`
- `([' ab', 'ab'], 'ab') -> 1`
- `(['ab', 'ab'], 'ab') -> 2`
- `(['xab', 'abx'], 'ab') -> 1`
- `(['\u00e9', 'e\u0301'], 'e') -> 1`
- `(['a'], 'abc') -> 0`
- `(['x'],'x'.repeat(64)) -> 0`
- `(['\ud800z'],'\ud800') -> 1`
- `(['a'],'x'.repeat(65)) -> RangeError`
- `([1],'a') -> TypeError`
- `([1],'x'.repeat(65)) -> TypeError`
- `(Array(1),'x'.repeat(65)) -> TypeError`
- `(['a'],1) -> TypeError`
- `(['a'],new String('a')) -> TypeError`
- `([new String('a')],'a') -> TypeError`
- `(['a'],null) -> TypeError`
- `(new Proxy(['a'],{}),'a') -> TypeError`

Only edit prefix_count.mjs and optional IMPLEMENTATION.md in this task directory.
Quick run from the repository root (Node 22):
`node tasks/prefix-count/check.mjs --solution "$PWD/tasks/prefix-count/prefix_count.mjs"`
The issue supplies a separate trusted checker pin and offline Docker command.
A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
