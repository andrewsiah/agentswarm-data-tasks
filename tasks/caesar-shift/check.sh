set -eu
if [ "$#" != 2 ] || [ "$1" != --solution ]; then echo 'expected --solution FILE' >&2; exit 2; fi
here=$(cd -- "$(dirname -- "$0")" && pwd)
build=$(mktemp -d)
trap 'rm -rf -- "$build"' EXIT
mkdir -p "$build/src" "$build/tests"
cp -- "$2" "$build/src/lib.rs"
cp -- "$here/fixtures/cases.rs" "$build/tests/cases.rs"
printf '[package]\nname = "caesar_shift"\nversion = "0.1.0"\nedition = "2021"\n' > "$build/Cargo.toml"
cd -- "$build"
cargo test --offline --quiet
printf 'PASS caesar-shift: trusted cargo integration cases\n'
