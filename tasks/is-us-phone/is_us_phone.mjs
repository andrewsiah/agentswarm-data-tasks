const MAX_LENGTH = 1000;
const PHONE_LENGTH = 12;

function isAsciiDigit(code) {
  return code >= 0x30 && code <= 0x39;
}

export function isUsPhone(text) {
  // typeof is the only check that rejects boxed Strings, subclasses and
  // proxies without touching the value; it must precede the length check.
  if (typeof text !== "string") {
    throw new TypeError("text must be a primitive string");
  }
  if (text.length > MAX_LENGTH) {
    throw new RangeError("text must be at most 1000 UTF-16 code units");
  }
  if (text.length !== PHONE_LENGTH) {
    return false;
  }
  // Positions 3 and 7 are hyphens; every other position is an ASCII digit.
  for (let i = 0; i < PHONE_LENGTH; i++) {
    const code = text.charCodeAt(i);
    if (i === 3 || i === 7) {
      if (code !== 0x2d) return false;
    } else if (!isAsciiDigit(code)) {
      return false;
    }
  }
  return true;
}
