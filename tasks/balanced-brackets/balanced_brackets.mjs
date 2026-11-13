export function balancedBrackets(text) {
  if (typeof text !== "string") {
    throw new TypeError("text must be a primitive string");
  }
  if (text.length > 1000) {
    throw new RangeError("text must be at most 1000 code units");
  }
  const pairs = { ")": "(", "]": "[", "}": "{" };
  const stack = [];
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (ch === "(" || ch === "[" || ch === "{") {
      stack.push(ch);
    } else if (ch === ")" || ch === "]" || ch === "}") {
      if (stack.length === 0 || stack.pop() !== pairs[ch]) {
        return false;
      }
    }
  }
  return stack.length === 0;
}
