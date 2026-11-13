export function leetSpeak(text: unknown): string {
  if (typeof text !== "string") {
    throw new TypeError("text must be a string");
  }
  if (text.length > 1000) {
    throw new RangeError("text is too long");
  }
  let out = "";
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (ch === "a") {
      out += "4";
    } else if (ch === "e") {
      out += "3";
    } else if (ch === "i") {
      out += "1";
    } else if (ch === "o") {
      out += "0";
    } else if (ch === "s") {
      out += "5";
    } else {
      out += ch;
    }
  }
  return out;
}
