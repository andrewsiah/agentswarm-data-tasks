# Write tests for a letter grade function

Write `tests_submission.py` using Python 3.11+ standard library unittest. The
provided `implementation.py` exports `letter_grade(score)`. Do not change it.
Only edit tests_submission.py and optional IMPLEMENTATION.md in this task.
Import `letter_grade` from `implementation`; use unittest.TestCase subclasses.
No third-party packages, files, subprocesses, networking or implementation
source inspection. Tests must assert public behavior, not identify a mutant.
They run without the task checker on their import path.

score must have exact built-in int type. Bool, int subclasses, floats, strings,
None and containers raise TypeError. Check the type before the range, so -1.0
raises TypeError. score below 0 or above 100 raises ValueError; 0 and 100 are
valid. Otherwise return an exact one-character uppercase str: 'A' for 90-100,
'B' for 80-89, 'C' for 70-79, 'D' for 60-69 and 'F' for 0-59. Every lower bound
is inclusive (90 is 'A', 80 is 'B', 70 is 'C', 60 is 'D'). There is no 'E'
grade and no plus or minus suffix. Calls are deterministic; no mutable state or
side effects. Exception messages are unconstrained.

Examples: letter_grade(100) == 'A'; letter_grade(90) == 'A';
letter_grade(89) == 'B'; letter_grade(70) == 'C'; letter_grade(65) == 'D';
letter_grade(59) == 'F'; letter_grade(0) == 'F'. letter_grade(101) and
letter_grade(-1) raise ValueError; letter_grade(True) and letter_grade(85.0)
raise TypeError.

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

Run `python3 tasks/grade-tests/check.py --solution "$PWD/tasks/grade-tests/tests_submission.py"`.
The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED
until independent source/scope review.
