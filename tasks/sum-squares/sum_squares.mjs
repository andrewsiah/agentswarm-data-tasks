import { types } from "node:util";

export function sumSquares(values) {
  if (types.isProxy(values)) {
    throw new TypeError("values must be a normal Array, not a Proxy");
  }
  if (!Array.isArray(values)) {
    throw new TypeError("values must be an Array");
  }
  if (Object.getPrototypeOf(values) !== Array.prototype) {
    throw new TypeError("values must have exactly Array.prototype as its prototype");
  }
  const len = values.length;
  for (let i = 0; i < len; i++) {
    if (!Object.prototype.hasOwnProperty.call(values, i)) {
      throw new TypeError("values must be dense: every index must be an own property");
    }
  }
  for (let i = 0; i < len; i++) {
    if (typeof values[i] !== "number") {
      throw new TypeError("every element must be a primitive number");
    }
  }
  let total = 0n;
  for (let i = 0; i < len; i++) {
    const v = values[i];
    if (!Number.isInteger(v) || v > 1e7 || v < -1e7) {
      throw new RangeError("every element must be an integer with absolute value at most 1e7");
    }
    total += BigInt(v) * BigInt(v);
  }
  if (total > BigInt(Number.MAX_SAFE_INTEGER)) {
    throw new RangeError("the exact sum exceeds Number.MAX_SAFE_INTEGER");
  }
  return Number(total);
}
