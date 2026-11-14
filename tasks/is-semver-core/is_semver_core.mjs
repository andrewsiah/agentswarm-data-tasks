export function isSemverCore(text) {
  if (typeof text !== "string") {
    throw new TypeError("text must be a primitive string");
  }
  if (text.length > 1000) {
    throw new RangeError("text must be at most 1000 code units long");
  }
  let dots = 0;
  let partLength = 0;
  let partStartsWithZero = false;
  for (let i = 0; i < text.length; i++) {
    const code = text.charCodeAt(i);
    if (code === 46) {
      // "." separator: the part just ended must be non-empty and valid.
      if (partLength === 0) return false;
      if (partLength > 1 && partStartsWithZero) return false;
      dots++;
      if (dots > 2) return false;
      partLength = 0;
      partStartsWithZero = false;
    } else if (code >= 48 && code <= 57) {
      // ASCII digit.
      if (partLength === 0 && code === 48) partStartsWithZero = true;
      partLength++;
    } else {
      return false;
    }
  }
  if (dots !== 2) return false;
  if (partLength === 0) return false;
  if (partLength > 1 && partStartsWithZero) return false;
  return true;
}
