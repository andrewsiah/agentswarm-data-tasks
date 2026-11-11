# Reverse the runes of a string

Implement `Reverse(s string) string` in package `reverse`, file `reverse.go`.
Use Go 1.23 standard library only. The supplied go.mod has no external
modules. Only edit reverse.go and optional IMPLEMENTATION.md in this task. Do
not change the checker, module, fixtures or specification. No file, clock or
network access.

Decode s into runes (Unicode code points) exactly as a Go `[]rune(s)`
conversion does, so each invalid UTF-8 byte becomes one U+FFFD rune. Return
the string whose runes are those runes in reverse order (as `string(runes)`
encodes them). Reverse code points, not bytes and not user-perceived
characters: a combining mark or emoji modifier moves to the other side of its
base character. Keep every rune exactly: no trimming, case change or Unicode
normalization. The empty string returns the empty string.

Examples: "" -> ""; "abc" -> "cba"; " ab " -> " ba "; "café" -> "éfac";
"日本語" -> "語本日"; "a🚀b" -> "b🚀a"; "e\u0301" -> "\u0301e";
"a\xffb" -> "b\uFFFDa".

The checker is Go code that copies only the candidate into an isolated temporary
module and compiles and runs trusted tests. Preload the digest-pinned golang
Docker image shown in the issue. Acceptance runs with --network none,
GOPROXY=off and GOSUMDB=off; no dependencies are downloaded. A cold Go build
may take about a minute. A pass remains CHECK_PASS_UNVERIFIED until independent
source/scope review.
