pub fn squash_repeats(input: &str) -> String {
    let mut output = String::with_capacity(input.len());
    let mut previous = None;

    for current in input.chars() {
        if previous != Some(current) {
            output.push(current);
            previous = Some(current);
        }
    }

    output
}
