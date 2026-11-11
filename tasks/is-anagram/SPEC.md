# Anagram check by code points

Implement export function isAnagram(a, b) in is_anagram.mjs, Node 22 standard
library only.

a and b must both be primitive strings; boxed String objects (also
subclasses), missing arguments and all other values raise exact TypeError.
Validate both types before any length check. Then a string longer than 1000
UTF-16 code units (its .length) raises exact RangeError.

Return the primitive boolean true when b is a rearrangement of a: every
Unicode code point occurs the same number of times in both strings. A
surrogate pair is one code point; a lone surrogate is its own code point.
Matching is case-sensitive and spaces and punctuation count. No trimming or
normalization (é and e + U+0301 differ). A string is an anagram of itself and
two empty strings are anagrams.

Error messages are unconstrained. Keep no state between calls; repeated and
independent calls return the same result.

Examples (arguments -> result); every one is checked:
- `('listen', 'silent') -> true`
- `('', '') -> true`
- `('a', 'a') -> true`
- `('ab', 'a') -> false`
- `('aab', 'abb') -> false`
- `('Listen', 'silent') -> false`
- `('dormitory', 'dirty room') -> false`
- `('a b', 'ba ') -> true`
- `('\u00e9', 'e\u0301') -> false`
- `('\ud83d\ude80\ud83e\udd16', '\ud83e\udd16\ud83d\ude80') -> true`
- `('abc', 'abd') -> false`
- `('\ud83d\ude80\ud83e\udd16','\ud83d\udd16\ud83e\ude80') -> false`
- `('\ud83d','\ud83d') -> true`
- `('\ud83d\ude80','\ude80\ud83d') -> false`
- `('\ud83dx','x\ud83d') -> true`
- `(1,'a') -> TypeError`
- `('a',null) -> TypeError`
- `(new String('a'),'a') -> TypeError`
- `('a'.repeat(1001),'a') -> RangeError`
- `('a','b'.repeat(1001)) -> RangeError`
- `('a'.repeat(1001),5) -> TypeError`
- `('\ud83d\ude80'.repeat(501),'') -> RangeError`

Only edit is_anagram.mjs and optional IMPLEMENTATION.md in this task directory.
Quick run from the repository root (Node 22):
`node tasks/is-anagram/check.mjs --solution "$PWD/tasks/is-anagram/is_anagram.mjs"`
The issue supplies a separate trusted checker pin and offline Docker command.
A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
