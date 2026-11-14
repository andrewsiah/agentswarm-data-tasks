// Returns true only for a US phone number in exactly the form NNN-NNN-NNNN
// (12 characters: 3 ASCII digits, "-", 3 ASCII digits, "-", 4 ASCII digits).
// No state is kept between calls.

const HYPHEN = 0x2d; // "-"
const ZERO = 0x30; // "0"
const NINE = 0x39; // "9"
const MAX_LENGTH = 1000;
const PHONE_LENGTH = 12;

function isAsciiDigit(code) {
  return code >= ZERO && code <= NINE;
}

export function isUsPhone(text) {
  if (typeof text !== 'string') {
    throw new TypeError('isUsPhone expects a primitive string');
  }
  if (text.length > MAX_LENGTH) {
    throw new RangeError(`isUsPhone input exceeds ${MAX_LENGTH} UTF-16 code units`);
  }
  if (text.length !== PHONE_LENGTH) {
    return false;
  }
  for (let i = 0; i < PHONE_LENGTH; i += 1) {
    const code = text.charCodeAt(i);
    if (i === 3 || i === 7) {
      if (code !== HYPHEN) {
        return false;
      }
    } else if (!isAsciiDigit(code)) {
      return false;
    }
  }
  return true;
}
