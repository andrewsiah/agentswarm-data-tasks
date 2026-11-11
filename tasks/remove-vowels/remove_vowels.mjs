export function removeVowels(text) {
  if (typeof text !== "string") {
    throw new TypeError("text must be a primitive string");
  }

  if (text.length > 1000) {
    throw new RangeError("text must not exceed 1000 UTF-16 code units");
  }

  return text.replace(/[aeiou]/gi, "");
}
