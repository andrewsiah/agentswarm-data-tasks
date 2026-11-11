# Validate a digit string with the Luhn checksum

Implement `pub fn luhn_valid(input: &str) -> bool` in `src/lib.rs` (crate
`luhn_check`). Rust 2021, standard library only, no crates. Only edit
src/lib.rs and optional IMPLEMENTATION.md in this task. Do not change the
checker, Cargo.toml, fixtures or this specification.

input may contain only ASCII digits 0-9 and ASCII spaces (U+0020). Spaces are
ignored anywhere. Any other character (letters, punctuation such as '-',
tabs, newlines, non-breaking spaces, non-ASCII digits) makes the result false.
After removing spaces, fewer than two digits is false (so "0" and "   " are
false, but "0 0" is true).

Otherwise apply the Luhn checksum: starting from the RIGHTMOST digit, double
every second digit (the second-from-right, fourth-from-right and so on); when
a doubled value exceeds 9 subtract 9. Sum all resulting digits. Return true
exactly when the sum is divisible by 10. Any input length must work without
panic or overflow.

Examples (input -> result):
- `"59"` -> `true`
- `"059"` -> `true`
- `"4539 3195 0343 6467"` -> `true`
- `"8273 1232 7352 0569"` -> `false`
- `"79927398713"` -> `true`
- `"0 0"` -> `true`
- `"0"` -> `false`
- `"055-444-285"` -> `false`
- `"\t59"` -> `false`

The checker copies only src/lib.rs into a fresh temporary crate and runs
trusted integration tests with `cargo test --offline`. Preload the
digest-pinned rust Docker image shown in the issue; acceptance runs with
--network none. A cold build may take about a minute. A pass remains
CHECK_PASS_UNVERIFIED until independent source/scope review.
