use isogram::is_isogram;
#[test]
fn spec_cases() {
assert_eq!(is_isogram(""),true,"''");
assert_eq!(is_isogram("a"),true,"'a'");
assert_eq!(is_isogram("z"),true,"'z'");
assert_eq!(is_isogram("isogram"),true,"'isogram'");
assert_eq!(is_isogram("eleven"),false,"'eleven'");
assert_eq!(is_isogram("Alphabet"),false,"'Alphabet'");
assert_eq!(is_isogram("subdermatoglyphic"),true,"'subdermatoglyphic'");
assert_eq!(is_isogram("six-year-old"),true,"'six-year-old'");
assert_eq!(is_isogram("thumbscrew-japingly"),true,"'thumbscrew-japingly'");
assert_eq!(is_isogram("Emily Jung Schwartzkopf"),true,"'Emily Jung Schwartzkopf'");
assert_eq!(is_isogram("aA"),false,"'aA'");
assert_eq!(is_isogram("zZ"),false,"'zZ'");
assert_eq!(is_isogram("a a"),false,"'a a'");
assert_eq!(is_isogram("a-a"),false,"'a-a'");
assert_eq!(is_isogram("11 22"),true,"'11 22'");
assert_eq!(is_isogram("--  --"),true,"'--  --'");
assert_eq!(is_isogram("é é"),true,"'é é'");
assert_eq!(is_isogram("éa"),true,"'éa'");
assert_eq!(is_isogram("ÉÉ"),true,"'ÉÉ'");
assert_eq!(is_isogram("ßß"),true,"'ßß'");
assert_eq!(is_isogram("İi"),true,"'İi'");
assert_eq!(is_isogram("background"),true,"'background'");
assert_eq!(is_isogram("accentor"),false,"'accentor'");
assert_eq!(is_isogram("up-to-date"),false,"'up-to-date'");
assert_eq!(is_isogram("ab\nba"),false,"'ab\\nba'");
assert_eq!(is_isogram("abcdefghijklmnopqrstuvwxyz"),true,"'abcdefghijklmnopqrstuvwxyz'");
assert_eq!(is_isogram("abcdefghijklmnopqrstuvwxyza"),false,"'abcdefghijklmnopqrstuvwxyza'");
assert_eq!(is_isogram("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),true,"'ABCDEFGHIJKLMNOPQRSTUVWXYZ'");
assert_eq!(is_isogram("abcABC"),false,"'abcABC'");
assert_eq!(is_isogram("Dermatoglyphics"),true,"'Dermatoglyphics'");
assert_eq!(is_isogram("\tq\tw"),true,"'\\tq\\tw'");
assert_eq!(is_isogram("0123456789"),true,"'0123456789'");
assert_eq!(is_isogram("x9x"),false,"'x9x'");
assert_eq!(is_isogram("ab"),true,"'ab'");
assert_eq!(is_isogram("aba"),false,"'aba'");
assert_eq!(is_isogram("abca"),false,"'abca'");
assert_eq!(is_isogram("àa"),true,"'àa'");
assert_eq!(is_isogram("a\u{300}"),true,"'a\u{300}'");
let dashes="- ".repeat(5000);assert_eq!(is_isogram(&dashes),true);
let tail=format!("{}q", "1".repeat(10000));assert_eq!(is_isogram(&tail),true);
let late=format!("q{}Q", "é".repeat(5000));assert_eq!(is_isogram(&late),false);
for _ in 0..3 {assert!(is_isogram("isogram"));assert!(!is_isogram("isograms"));}
}
