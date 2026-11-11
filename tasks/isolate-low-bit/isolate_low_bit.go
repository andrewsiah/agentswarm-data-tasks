package isolatelowbit

func IsolateLowBit(n uint32) uint32 {
	return n & -n
}
