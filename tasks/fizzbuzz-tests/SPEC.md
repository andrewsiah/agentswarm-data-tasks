# Write tests for a FizzBuzz word function

Write `tests_submission.py` using Python 3.11+ standard library unittest. The
provided `implementation.py` exports `fizzbuzz(n)`. Do not change it.
Only edit tests_submission.py and optional IMPLEMENTATION.md in this task.
Import `fizzbuzz` from `implementation`; use unittest.TestCase subclasses.
No third-party packages, files, subprocesses, networking or implementation
source inspection. Tests must assert public behavior, not identify a mutant.
They run without the task checker on their import path.

n must have exact built-in int type. Bool, int subclasses, floats, strings,
None and containers raise TypeError. Check the type before the range, so -3.0
raises TypeError. n below 1 (0 and negatives) raises ValueError. Otherwise
return an exact str: 'FizzBuzz' when n is divisible by both 3 and 5 (that is,
by 15), else 'Fizz' when divisible by 3, else 'Buzz' when divisible by 5, else
the decimal digits of n as a str (str(n)). Capitalization is exact and there
is no space inside 'FizzBuzz'. Integers are arbitrary precision for the
divisibility rules; the plain-number result is exactly Python's built-in
str(n), so, like str(n), it raises ValueError when n has more decimal digits
than Python's default 4300-digit conversion limit. Calls are deterministic; no mutable state or side effects. Exception messages are
unconstrained.

Examples: fizzbuzz(1) == '1'; fizzbuzz(3) == 'Fizz'; fizzbuzz(5) == 'Buzz';
fizzbuzz(15) == 'FizzBuzz'; fizzbuzz(10) == 'Buzz'; fizzbuzz(98) == '98'.
fizzbuzz(0) raises ValueError; fizzbuzz(True) and fizzbuzz(3.0) raise
TypeError.

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

Run `python3 tasks/fizzbuzz-tests/check.py --solution "$PWD/tasks/fizzbuzz-tests/tests_submission.py"`.
The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED
until independent source/scope review.
