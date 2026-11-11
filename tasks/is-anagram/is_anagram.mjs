// isAnagram(a, b): true when two primitive strings hold the same Unicode
// code points the same number of times. See SPEC.md.
//
// Both arguments must be primitive strings (boxed String objects and every
// other value raise TypeError); both types are validated before any length
// check. A string longer than 1000 UTF-16 code units raises RangeError.
// Comparison is by code point: a surrogate pair is one code point and a
// lone surrogate is its own code point. Case-sensitive; no trimming or
// normalization. No state is kept between calls.

const MAX_CODE_UNITS = 1000;

export function isAnagram(a, b) {
  if (typeof a !== "string" || typeof b !== "string") {
    throw new TypeError("both arguments must be primitive strings");
  }
  if (a.length > MAX_CODE_UNITS || b.length > MAX_CODE_UNITS) {
    throw new RangeError("string longer than 1000 UTF-16 code units");
  }
  const counts = new Map();
  for (const ch of a) {
    counts.set(ch, (counts.get(ch) ?? 0) + 1);
  }
  for (const ch of b) {
    const remaining = counts.get(ch);
    if (remaining === undefined) {
      return false;
    }
    if (remaining === 1) {
      counts.delete(ch);
    } else {
      counts.set(ch, remaining - 1);
    }
  }
  return counts.size === 0;
}
