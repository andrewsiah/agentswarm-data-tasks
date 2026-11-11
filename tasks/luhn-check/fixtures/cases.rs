use luhn_check::luhn_valid;
#[test]
fn spec_cases() {
assert_eq!(luhn_valid(""),false,"''");
assert_eq!(luhn_valid("0"),false,"'0'");
assert_eq!(luhn_valid(" 0"),false,"' 0'");
assert_eq!(luhn_valid("   "),false,"'   '");
assert_eq!(luhn_valid("0 0"),true,"'0 0'");
assert_eq!(luhn_valid("00"),true,"'00'");
assert_eq!(luhn_valid("59"),true,"'59'");
assert_eq!(luhn_valid("18"),true,"'18'");
assert_eq!(luhn_valid("091"),true,"'091'");
assert_eq!(luhn_valid("059"),true,"'059'");
assert_eq!(luhn_valid("4539 3195 0343 6467"),true,"'4539 3195 0343 6467'");
assert_eq!(luhn_valid("8273 1232 7352 0569"),false,"'8273 1232 7352 0569'");
assert_eq!(luhn_valid("79927398713"),true,"'79927398713'");
assert_eq!(luhn_valid("79927398710"),false,"'79927398710'");
assert_eq!(luhn_valid("055 444 285"),true,"'055 444 285'");
assert_eq!(luhn_valid("055-444-285"),false,"'055-444-285'");
assert_eq!(luhn_valid("055a 444 285"),false,"'055a 444 285'");
assert_eq!(luhn_valid(":9"),false,"':9'");
assert_eq!(luhn_valid("\t59"),false,"'\\t59'");
assert_eq!(luhn_valid("59\n"),false,"'59\\n'");
assert_eq!(luhn_valid("٣٣"),false,"'٣٣'");
assert_eq!(luhn_valid("1234567812345670"),true,"'1234567812345670'");
assert_eq!(luhn_valid("1234567812345678"),false,"'1234567812345678'");
assert_eq!(luhn_valid("4111 1111 1111 1111"),true,"'4111 1111 1111 1111'");
assert_eq!(luhn_valid("4111111111111112"),false,"'4111111111111112'");
assert_eq!(luhn_valid("  5 9  "),true,"'  5 9  '");
assert_eq!(luhn_valid("\u{a0}59"),false,"'\\xa059'");
assert_eq!(luhn_valid("3"),false,"'3'");
assert_eq!(luhn_valid("9999999999"),true,"'9999999999'");
assert_eq!(luhn_valid("99999999999"),false,"'99999999999'");
assert_eq!(luhn_valid("1 2 3 4 5 6 7 8 9 0"),false,"'1 2 3 4 5 6 7 8 9 0'");
assert_eq!(luhn_valid("12345674"),true,"'12345674'");
assert_eq!(luhn_valid("0000 0000 0000 0000"),true,"'0000 0000 0000 0000'");
let zeros="0 ".repeat(5000);assert_eq!(luhn_valid(&zeros),true);
let nines="9".repeat(1001);assert_eq!(luhn_valid(&nines),false);
for _ in 0..3 {assert!(luhn_valid("79927398713"));assert!(!luhn_valid("79927398710"));}
}
