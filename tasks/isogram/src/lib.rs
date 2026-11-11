pub fn is_isogram(input: &str) -> bool {
    let mut seen = [false; 26];
    for c in input.chars() {
        if c.is_ascii_alphabetic() {
            let idx = c.to_ascii_lowercase() as usize - 'a' as usize;
            if seen[idx] {
                return false;
            }
            seen[idx] = true;
        }
    }
    true
}
