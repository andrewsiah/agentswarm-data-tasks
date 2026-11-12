// Return true when the Unicode code points of a occur in b in the same
// order (not necessarily contiguously). Both arguments must be primitive
// strings; anything else raises TypeError. A string longer than 1000 UTF-16
// code units raises RangeError. Code points come from the string iterator,
// so a surrogate pair is one code point and a lone surrogate is its own.
export function isSubsequence(a, b) {
  if (typeof a !== "string" || typeof b !== "string") {
    throw new TypeError("both arguments must be primitive strings");
  }
  if (a.length > 1000 || b.length > 1000) {
    throw new RangeError("strings must be at most 1000 UTF-16 code units");
  }
  const aPoints = Array.from(a);
  const bPoints = Array.from(b);
  let i = 0;
  for (let j = 0; j < bPoints.length && i < aPoints.length; j += 1) {
    if (bPoints[j] === aPoints[i]) {
      i += 1;
    }
  }
  return i === aPoints.length;
}
