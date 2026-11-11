# Rotate ASCII letters by a signed shift

Implement `pub fn caesar_shift(input: &str, shift: i32) -> String` in
`src/lib.rs` (crate `caesar_shift`). Rust 2021, standard library only, no
crates. Only edit src/lib.rs and optional IMPLEMENTATION.md in this task. Do
not change the checker, Cargo.toml, fixtures or this specification.

Move every ASCII letter forward in the alphabet by shift places, wrapping
around: a-z stays lowercase and A-Z stays uppercase (z + 1 is a, Z + 1 is A).
A negative shift moves backward (a - 1 is z). Any i32 is valid, including
i32::MIN and i32::MAX; only shift modulo 26 (Euclidean, always 0 to 25)
matters, so 27 behaves like 1 and -1 behaves like 25. Do not panic or
overflow.

Every other character is copied unchanged: digits, spaces, punctuation, tabs,
newlines, NUL and all non-ASCII characters including accented letters and
emoji (no Unicode case mapping, no normalization). The output has the same
number of chars as the input.

Examples (input, shift -> output):
- `"abc", 1` -> `"bcd"`
- `"xyz", 3` -> `"abc"`
- `"Hello, World!", 13` -> `"Uryyb, Jbeyq!"`
- `"Hello, World!", -13` -> `"Uryyb, Jbeyq!"`
- `"ABC xyz", 27` -> `"BCD yza"`
- `"abc", -1` -> `"zab"`
- `"Zebra 123", 2` -> `"Bgdtc 123"`
- `"élan vital", 1` -> `"émbo wjubm"`
- `"MixedCase", -2147483648` -> `"OkzgfEcug"`

The checker copies only src/lib.rs into a fresh temporary crate and runs
trusted integration tests with `cargo test --offline`. Preload the
digest-pinned rust Docker image shown in the issue; acceptance runs with
--network none. A cold build may take about a minute. A pass remains
CHECK_PASS_UNVERIFIED until independent source/scope review.
