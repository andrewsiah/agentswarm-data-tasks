// Converts snake_case to camelCase: every "_" is removed and a character that
// directly follows an underscore is uppercased only when it is an ASCII
// lowercase letter a-z. Everything else is copied unchanged, in order
// (uppercase stays uppercase, no lowercasing, digits/emoji/lone surrogates and
// non-ASCII letters are untouched, the first character is never capitalized
// unless it follows an underscore). No state is kept between calls.

const UNDERSCORE = 0x5f; // "_"
const LOWER_A = 0x61; // "a"
const LOWER_Z = 0x7a; // "z"
const CASE_OFFSET = 0x20; // "a" - "A"
const MAX_LENGTH = 1000;

export function snakeToCamel(text) {
  if (typeof text !== 'string') {
    throw new TypeError('snakeToCamel expects a primitive string');
  }
  if (text.length > MAX_LENGTH) {
    throw new RangeError(`snakeToCamel input exceeds ${MAX_LENGTH} UTF-16 code units`);
  }
  let result = '';
  let afterUnderscore = false;
  for (let i = 0; i < text.length; i += 1) {
    const code = text.charCodeAt(i);
    if (code === UNDERSCORE) {
      afterUnderscore = true;
      continue;
    }
    if (afterUnderscore) {
      afterUnderscore = false;
      if (code >= LOWER_A && code <= LOWER_Z) {
        result += String.fromCharCode(code - CASE_OFFSET);
        continue;
      }
    }
    result += String.fromCharCode(code);
  }
  return result;
}
