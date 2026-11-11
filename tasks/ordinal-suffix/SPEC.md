# Format integers as English ordinals

Implement `Ordinal(n int) string` in package `ordinal`, file `ordinal.go`.
Use Go 1.23 standard library only. The supplied go.mod has no external
modules. Only edit ordinal.go and optional IMPLEMENTATION.md in this task. Do
not change the checker, module, fixtures or specification. No file, clock or
network access.

For n >= 0 return the decimal digits of n (no sign, separators or padding)
followed directly by a lowercase suffix: `st` when n ends in 1, `nd` when it
ends in 2, `rd` when it ends in 3 and `th` otherwise, EXCEPT that numbers whose
last two digits are 11, 12 or 13 always take `th` (11th, 112th, 1013th). Zero
is `0th`. Any negative n, including the int64 minimum, returns exactly the
lowercase word `invalid`. No spaces between number and suffix.

Examples: 0 -> `0th`; 1 -> `1st`; 2 -> `2nd`; 3 -> `3rd`; 4 -> `4th`;
11 -> `11th`; 12 -> `12th`; 13 -> `13th`; 21 -> `21st`; 22 -> `22nd`;
101 -> `101st`; 111 -> `111th`; 112 -> `112th`; 1003 -> `1003rd`;
-1 -> `invalid`.

The checker is Go code that copies only the candidate into an isolated temporary
module and compiles and runs trusted tests. Preload the digest-pinned golang
Docker image shown in the issue. Acceptance runs with --network none,
GOPROXY=off and GOSUMDB=off; no dependencies are downloaded. A cold Go build
may take about a minute. A pass remains CHECK_PASS_UNVERIFIED until independent
source/scope review.
