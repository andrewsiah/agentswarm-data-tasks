package hamming

// Hamming returns the number of positions at which the Unicode code points in
// a and b differ. If the strings contain different numbers of code points, it
// returns -1.
func Hamming(a, b string) int {
	aRunes := []rune(a)
	bRunes := []rune(b)
	if len(aRunes) != len(bRunes) {
		return -1
	}

	differences := 0
	for i, aRune := range aRunes {
		if aRune != bRunes[i] {
			differences++
		}
	}
	return differences
}
