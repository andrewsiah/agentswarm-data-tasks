# is-palindrome
Implement `is_palindrome` in `is_palindrome.py`. Python 3.11+ standard library only.

Require text, an exact built-in str of at most 1000 Unicode code points. Keep only the ASCII letters a-z and A-Z and the ASCII digits 0-9 of text, in order, and compare letters case-insensitively (A equals a). Every other character, including spaces, punctuation, non-ASCII letters such as é and non-ASCII digits, is ignored. Return the exact bool True when the kept characters read the same forwards and backwards, otherwise the exact bool False. When nothing is kept (for example "" or "?!"), return True.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `['']` -> `True`
- `['a']` -> `True`
- `['abba']` -> `True`
- `['abc']` -> `False`
- `['Racecar']` -> `True`
- `['A man, a plan, a canal: Panama']` -> `True`
- `['No lemon, no melon']` -> `True`
- `['ab']` -> `False`
- `['12321']` -> `True`
- `['123ab']` -> `False`
- `['1a2']` -> `False`
- `['abca']` -> `False`
- `['?!']` -> `True`
- `['éa']` -> `True`
- `['ab é ba']` -> `True`
- `['a٣b']` -> `False`
- `[['a']]` -> `raises TypeError`
- `['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']` -> `raises ValueError`

Only edit `is_palindrome.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/is-palindrome/check.py --solution "$PWD/tasks/is-palindrome/is_palindrome.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
