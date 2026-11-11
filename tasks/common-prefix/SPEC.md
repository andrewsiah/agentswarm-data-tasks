# Longest common prefix by code points

Implement export function commonPrefix(values) in common_prefix.mjs, Node 22
standard library only.

values must be a dense normal Array: prototype exactly Array.prototype, not a
Proxy (use types.isProxy from node:util; this includes revoked proxies), and
every index an own property. Reject subclasses, altered prototypes, nonarrays
and holes with exact TypeError. Every element must be a primitive string; boxed
String objects (also subclasses) and all other values raise exact TypeError.
Validate ALL types before the length check: an empty array then raises exact
RangeError.

Return the longest string that every element starts with, compared by Unicode
code points. Never split a surrogate pair: when elements share a high
surrogate but not the full code point, drop it (so the prefix of an emoji and
a lone high surrogate is ''). Lone surrogates are ordinary code points.
Matching is case-sensitive with no trimming or normalization (e + U+0301 and
é differ). A one-element array returns that element.

Error messages are unconstrained. Never change input values or properties;
frozen arrays are supported. Ignore extra named array properties and never call
user-shadowed array methods or the input's iterator (use index loops). Index
properties are ordinary data properties. Independent calls return independent
results.

Examples (arguments -> result); every one is checked:
- `(['a']) -> 'a'`
- `(['flower', 'flow', 'flight']) -> 'fl'`
- `(['dog', 'racecar']) -> ''`
- `(['abc', 'abc']) -> 'abc'`
- `(['ab', 'abc']) -> 'ab'`
- `(['', 'abc']) -> ''`
- `(['Ab', 'ab']) -> ''`
- `(['interview', 'internet', 'interval']) -> 'inter'`
- `(['\u00e9', 'e\u0301']) -> ''`
- `(['e\u0301x', 'e\u0301y']) -> 'e\u0301'`
- `(['\ud83d\ude80','\ud83d\ude81']) -> ''`
- `(['\ud83d','\ud83d\ude80']) -> ''`
- `(['\ud83d\ude80a','\ud83d\ude80b']) -> '\ud83d\ude80'`
- `(['\ud83dx','\ud83dy']) -> '\ud83d'`
- `([]) -> RangeError`
- `([1]) -> TypeError`
- `([new String('a')]) -> TypeError`
- `(Array(1)) -> TypeError`
- `(['a',null]) -> TypeError`
- `(new Proxy(['a'],{})) -> TypeError`

Only edit common_prefix.mjs and optional IMPLEMENTATION.md in this task directory.
Quick run from the repository root (Node 22):
`node tasks/common-prefix/check.mjs --solution "$PWD/tasks/common-prefix/common_prefix.mjs"`
The issue supplies a separate trusted checker pin and offline Docker command.
A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
