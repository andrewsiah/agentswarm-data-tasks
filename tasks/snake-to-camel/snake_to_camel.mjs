export function snakeToCamel(text) {
  if (typeof text !== "string") {
    throw new TypeError("text must be a primitive string");
  }
  if (text.length > 1000) {
    throw new RangeError("text must be at most 1000 code units");
  }
  let result = "";
  let afterUnderscore = false;
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (ch === "_") {
      afterUnderscore = true;
    } else {
      if (afterUnderscore && ch >= "a" && ch <= "z") {
        result += ch.toUpperCase();
      } else {
        result += ch;
      }
      afterUnderscore = false;
    }
  }
  return result;
}
