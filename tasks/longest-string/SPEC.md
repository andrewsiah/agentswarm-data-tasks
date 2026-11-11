# First longest string by code points

Implement export function longestString(values) in longest_string.mjs, Node 22
standard library only.

values must be a dense normal Array: prototype exactly Array.prototype, not a
Proxy (use types.isProxy from node:util; this includes revoked proxies), and
every index an own property. Reject subclasses, altered prototypes, nonarrays
and holes with exact TypeError. Every element must be a primitive string; boxed
String objects (also subclasses) and all other values raise exact TypeError.
Validate ALL types before the length check: an empty array then raises exact
RangeError.

Return the element (the string itself, not its index) with the most Unicode
code points. A surrogate pair such as an emoji counts as ONE code point and a
lone surrogate also counts as one; a combining sequence such as e + U+0301 is
two. Do not use .length (UTF-16 code units). On a tie the EARLIEST element
wins. Strings are opaque: no trimming or normalization.

Error messages are unconstrained. Never change input values or properties;
frozen arrays are supported. Ignore extra named array properties and never call
user-shadowed array methods or the input's iterator (use index loops). Index
properties are ordinary data properties. Independent calls return independent
results.

Examples (arguments -> result); every one is checked:
- `(['a']) -> 'a'`
- `(['a', 'bbb', 'cc']) -> 'bbb'`
- `(['ab', 'cd']) -> 'ab'`
- `(['', '']) -> ''`
- `(['x', 'yy', 'zz']) -> 'yy'`
- `(['ab ', 'abc']) -> 'ab '`
- `(['\u00e9', 'e']) -> '\u00e9'`
- `(['\ud83d\ude80', 'ab']) -> 'ab'`
- `(['e\u0301', 'ab', 'c']) -> 'e\u0301'`
- `(['\ud83d\ude80\ud83d\ude80','abc']) -> 'abc'`
- `(['\ud800\ud800','a']) -> '\ud800\ud800'`
- `([]) -> RangeError`
- `([1]) -> TypeError`
- `([new String('a')]) -> TypeError`
- `(Array(1)) -> TypeError`
- `(['a',null]) -> TypeError`
- `(new Proxy(['a'],{})) -> TypeError`

Only edit longest_string.mjs and optional IMPLEMENTATION.md in this task directory.
Quick run from the repository root (Node 22):
`node tasks/longest-string/check.mjs --solution "$PWD/tasks/longest-string/longest_string.mjs"`
The issue supplies a separate trusted checker pin and offline Docker command.
A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
