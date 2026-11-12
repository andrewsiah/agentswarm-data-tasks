// Return true exactly when text is a MAC address: six groups of exactly two
// ASCII hex digits separated by five separators that are all ":" or all "-".
// text must be a primitive string; anything else raises TypeError. A string
// longer than 1000 UTF-16 code units raises RangeError.
export function isMacAddress(text) {
  if (typeof text !== "string") {
    throw new TypeError("text must be a primitive string");
  }
  if (text.length > 1000) {
    throw new RangeError("text must be at most 1000 UTF-16 code units");
  }
  if (text.length !== 17) {
    return false;
  }
  const separator = text.charAt(2);
  if (separator !== ":" && separator !== "-") {
    return false;
  }
  const isHexDigit = (code) =>
    (code >= 48 && code <= 57) ||
    (code >= 65 && code <= 70) ||
    (code >= 97 && code <= 102);
  for (let i = 0; i < 17; i += 1) {
    if (i % 3 === 2) {
      if (text.charAt(i) !== separator) {
        return false;
      }
    } else if (!isHexDigit(text.charCodeAt(i))) {
      return false;
    }
  }
  return true;
}
