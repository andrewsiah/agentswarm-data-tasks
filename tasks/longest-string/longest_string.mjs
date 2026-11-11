import { types } from "node:util";

function codePointCount(s) {
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    const unit = s.charCodeAt(i);
    if (unit >= 0xd800 && unit <= 0xdbff && i + 1 < s.length) {
      const next = s.charCodeAt(i + 1);
      if (next >= 0xdc00 && next <= 0xdfff) {
        i++;
      }
    }
    count++;
  }
  return count;
}

export function longestString(values) {
  if (types.isProxy(values)) {
    throw new TypeError("values must not be a Proxy");
  }
  if (!Array.isArray(values)) {
    throw new TypeError("values must be an Array");
  }
  if (Object.getPrototypeOf(values) !== Array.prototype) {
    throw new TypeError("values must be a normal Array with Array.prototype");
  }
  const len = values.length;
  for (let i = 0; i < len; i++) {
    if (!Object.prototype.hasOwnProperty.call(values, i)) {
      throw new TypeError("values must be a dense Array");
    }
    if (typeof values[i] !== "string") {
      throw new TypeError("every element must be a primitive string");
    }
  }
  if (len === 0) {
    throw new RangeError("values must not be empty");
  }
  let best = values[0];
  let bestCount = codePointCount(best);
  for (let i = 1; i < len; i++) {
    const count = codePointCount(values[i]);
    if (count > bestCount) {
      best = values[i];
      bestCount = count;
    }
  }
  return best;
}
