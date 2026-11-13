export function isUsZip(text) {
  if (typeof text !== "string") {
    throw new TypeError("text must be a string");
  }
  if (text.length > 1000) {
    throw new RangeError("text is too long");
  }
  const isDigit = (ch) => ch >= "0" && ch <= "9";
  if (text.length === 5) {
    for (let i = 0; i < 5; i++) {
      if (!isDigit(text[i])) {
        return false;
      }
    }
    return true;
  }
  if (text.length === 10) {
    if (text[5] !== "-") {
      return false;
    }
    for (let i = 0; i < 10; i++) {
      if (i !== 5 && !isDigit(text[i])) {
        return false;
      }
    }
    return true;
  }
  return false;
}
