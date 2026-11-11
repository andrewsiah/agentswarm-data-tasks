# Write tests for a Gregorian leap-year check

Write `tests_submission.py` using Python 3.11+ standard library unittest. The
provided `implementation.py` exports `is_leap_year(year)`. Do not change it.
Only edit tests_submission.py and optional IMPLEMENTATION.md in this task.
Import `is_leap_year` from `implementation`; use unittest.TestCase subclasses.
No third-party packages, files, subprocesses, networking or implementation
source inspection. Tests must assert public behavior, not identify a mutant.
They run without the task checker on their import path.

year must have exact built-in int type. Bool, int subclasses, floats, strings,
None and containers raise TypeError. Check the type before the range, so -4.0
raises TypeError. A year below 1 (0 and negatives) raises ValueError. Otherwise
return the exact bool True when the year is a Gregorian leap year and False
otherwise: divisible by 4, except years divisible by 100, which are leap years
only when also divisible by 400. Integers are arbitrary precision. Calls are
deterministic; no mutable state or side effects. Exception messages are
unconstrained.

Examples: is_leap_year(2024) is True; is_leap_year(2023) is False;
is_leap_year(1900) is False; is_leap_year(2000) is True; is_leap_year(1) is
False; is_leap_year(4) is True. is_leap_year(0) raises ValueError;
is_leap_year(True) and is_leap_year(2024.0) raise TypeError.

Acceptance: at least eight discovered test methods, zero skipped tests and all
must pass against the provided reference implementation. The same tests then
run against ten supplied spec-contradicting implementations in fresh isolated
Python subprocesses. At least eight of ten must fail by a unittest assertion
failure or error. Empty suites, imports that fail before tests are discovered,
timeouts and system exits do not count as mutant kills. Never skip or mark
expected failures. The checker names the number of mutants killed; stronger
suites can kill all ten. Only the submitted test file is copied beside the
selected implementation; keep all helpers in that file. Each subprocess has
five seconds.

Run `python3 tasks/leap-tests/check.py --solution "$PWD/tasks/leap-tests/tests_submission.py"`.
The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED
until independent source/scope review.
