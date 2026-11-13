export function isUuid(text) {
  if (typeof text !== "string") {
    throw new TypeError("text must be a primitive string");
  }
  if (text.length > 1000) {
    throw new RangeError("text must be at most 1000 code units");
  }
  if (text.length !== 36) {
    return false;
  }
  for (let i = 0; i < 36; i++) {
    const ch = text[i];
    if (i === 8 || i === 13 || i === 18 || i === 23) {
      if (ch !== "-") {
        return false;
      }
    } else if (
      !(
        (ch >= "0" && ch <= "9") ||
        (ch >= "a" && ch <= "f") ||
        (ch >= "A" && ch <= "F")
      )
    ) {
      return false;
    }
  }
  return true;
}
