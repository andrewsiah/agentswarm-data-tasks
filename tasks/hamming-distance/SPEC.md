# Count differing runes between two strings

Implement `Hamming(a, b string) int` in package `hamming`, file `hamming.go`.
Use Go 1.23 standard library only. The supplied go.mod has no external
modules. Only edit hamming.go and optional IMPLEMENTATION.md in this task. Do
not change the checker, module, fixtures or specification. No file, clock or
network access.

Decode both strings into runes (Unicode code points) exactly as a Go
`[]rune(s)` conversion does, so each invalid UTF-8 byte becomes one U+FFFD
rune. When the two rune counts differ, return -1. Otherwise return how many
positions hold different runes. Comparison is exact and case-sensitive: no
case folding, trimming or Unicode normalization (é and e + U+0301 differ, and
so do their lengths). Byte lengths do not matter. The result is symmetric.

Examples: ("", "") -> 0; ("karolin", "kathrin") -> 3; ("Go", "go") -> 1;
("abc", "ab") -> -1; ("é", "e") -> 1; ("日本語", "日本人") -> 1;
("e\u0301", "é") -> -1; ("1011101", "1001001") -> 2.

The checker is Go code that copies only the candidate into an isolated temporary
module and compiles and runs trusted tests. Preload the digest-pinned golang
Docker image shown in the issue. Acceptance runs with --network none,
GOPROXY=off and GOSUMDB=off; no dependencies are downloaded. A cold Go build
may take about a minute. A pass remains CHECK_PASS_UNVERIFIED until independent
source/scope review.
