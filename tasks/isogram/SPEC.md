# Check whether a string repeats any ASCII letter

Implement `pub fn is_isogram(input: &str) -> bool` in `src/lib.rs` (crate
`isogram`). Rust 2021, standard library only, no crates. Only edit src/lib.rs
and optional IMPLEMENTATION.md in this task. Do not change the checker,
Cargo.toml, fixtures or this specification.

Only ASCII letters matter: a-z and A-Z, compared case-insensitively (a and A
are the same letter). Every other character is ignored and may repeat any
number of times: digits, spaces, hyphens, tabs, newlines, punctuation and all
non-ASCII characters, including accented letters such as é, combining marks
and non-ASCII letters that resemble ASCII ones. Return true when no ASCII
letter occurs more than once, otherwise false. The empty string and strings
without ASCII letters return true. Any input length must work without panic.

Examples (input -> result):
- `"isogram"` -> `true`
- `"eleven"` -> `false`
- `"Alphabet"` -> `false`
- `"six-year-old"` -> `true`
- `"Emily Jung Schwartzkopf"` -> `true`
- `"a a"` -> `false`
- `"éa"` -> `true`
- `"é é"` -> `true`
- `""` -> `true`

The checker copies only src/lib.rs into a fresh temporary crate and runs
trusted integration tests with `cargo test --offline`. Preload the
digest-pinned rust Docker image shown in the issue; acceptance runs with
--network none. A cold build may take about a minute. A pass remains
CHECK_PASS_UNVERIFIED until independent source/scope review.
