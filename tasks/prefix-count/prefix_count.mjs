import { types } from "node:util";

export function prefixCount(values, prefix) {
  if (types.isProxy(values)) {
    throw new TypeError("values must not be a Proxy");
  }
  if (!Array.isArray(values)) {
    throw new TypeError("values must be an Array");
  }
  if (Object.getPrototypeOf(values) !== Array.prototype) {
    throw new TypeError("values must be a normal Array with Array.prototype");
  }
  if (typeof prefix !== "string") {
    throw new TypeError("prefix must be a primitive string");
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
  if (prefix.length > 64) {
    throw new RangeError("prefix must be at most 64 UTF-16 code units");
  }
  let count = 0;
  for (let i = 0; i < len; i++) {
    const el = values[i];
    if (el.length < prefix.length) {
      continue;
    }
    let ok = true;
    for (let j = 0; j < prefix.length; j++) {
      if (el[j] !== prefix[j]) {
        ok = false;
        break;
      }
    }
    if (ok) {
      count++;
    }
  }
  return count;
}
