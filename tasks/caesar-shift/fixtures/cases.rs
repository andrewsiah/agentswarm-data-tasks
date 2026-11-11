use caesar_shift::caesar_shift;
#[test]
fn spec_cases() {
assert_eq!(caesar_shift("",5),"");
assert_eq!(caesar_shift("abc",1),"bcd");
assert_eq!(caesar_shift("xyz",3),"abc");
assert_eq!(caesar_shift("Hello, World!",13),"Uryyb, Jbeyq!");
assert_eq!(caesar_shift("Hello, World!",-13),"Uryyb, Jbeyq!");
assert_eq!(caesar_shift("ABC xyz",26),"ABC xyz");
assert_eq!(caesar_shift("ABC xyz",27),"BCD yza");
assert_eq!(caesar_shift("abc",-1),"zab");
assert_eq!(caesar_shift("abc",-27),"zab");
assert_eq!(caesar_shift("abc",52),"abc");
assert_eq!(caesar_shift("Zebra 123",2),"Bgdtc 123");
assert_eq!(caesar_shift("élan vital",1),"émbo wjubm");
assert_eq!(caesar_shift("straße ÄÖÜ",5),"xywfßj ÄÖÜ");
assert_eq!(caesar_shift("tab\tx",1),"ubc\ty");
assert_eq!(caesar_shift("🚀 rocket",4),"🚀 vsgoix");
assert_eq!(caesar_shift("a\u{a0}b",1),"b\u{a0}c");
assert_eq!(caesar_shift("MixedCase",i32::MAX),"JfubaZxpb");
assert_eq!(caesar_shift("MixedCase",i32::MIN),"OkzgfEcug");
assert_eq!(caesar_shift("āb ǅ",1),"āc ǅ");
assert_eq!(caesar_shift("Ωω zz",3),"Ωω cc");
assert_eq!(caesar_shift("e\u{301} Az",25),"d\u{301} Zy");
assert_eq!(caesar_shift("\u{0}nul",1),"\u{0}ovm");
assert_eq!(caesar_shift("AZ az",0),"AZ az");
assert_eq!(caesar_shift("09:59",7),"09:59");
let long="abc ".repeat(300);assert_eq!(caesar_shift(&long,1),"bcd ".repeat(300));
let mut first=caesar_shift("aa bb",1);first.clear();assert_eq!(caesar_shift("aa bb",1),"bb cc");
for shift in -60..60 {let s=caesar_shift("Az",shift);assert_eq!(caesar_shift(&s,-shift),"Az");}
}
