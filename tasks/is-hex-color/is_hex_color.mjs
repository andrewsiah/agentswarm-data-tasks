// Return true exactly when text is "#" followed by exactly three or exactly
// six ASCII hex digits (0-9, a-f, A-F, mixed case allowed). text must be a
// primitive string; anything else raises TypeError. A string longer than
// 1000 UTF-16 code units raises RangeError.
export function isHexColor(text) {
  if (typeof text !== "string") {
    throw new TypeError("text must be a primitive string");
  }
  if (text.length > 1000) {
    throw new RangeError("text must be at most 1000 UTF-16 code units");
  }
  if (text.length !== 4 && text.length !== 7) {
    return false;
  }
  if (text.charAt(0) !== "#") {
    return false;
  }
  const isHexDigit = (code) =>
    (code >= 48 && code <= 57) ||
    (code >= 65 && code <= 70) ||
    (code >= 97 && code <= 102);
  for (let i = 1; i < text.length; i += 1) {
    if (!isHexDigit(text.charCodeAt(i))) {
      return false;
    }
  }
  return true;
}
