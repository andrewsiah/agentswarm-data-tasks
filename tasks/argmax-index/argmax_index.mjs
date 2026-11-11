import { types } from "node:util";

export function argmaxIndex(values) {
  if (
    types.isProxy(values) ||
    !Array.isArray(values) ||
    Object.getPrototypeOf(values) !== Array.prototype
  ) {
    throw new TypeError("values must be a dense normal Array");
  }
  const len = values.length;
  for (let i = 0; i < len; i++) {
    if (!Object.hasOwn(values, i)) {
      throw new TypeError("values must be dense (no holes)");
    }
    if (typeof values[i] !== "number") {
      throw new TypeError("every element must be a primitive number");
    }
  }
  for (let i = 0; i < len; i++) {
    if (!Number.isSafeInteger(values[i])) {
      throw new RangeError("every element must be a safe integer");
    }
  }
  if (len === 0) {
    throw new RangeError("values must be nonempty");
  }
  let best = 0;
  for (let i = 1; i < len; i++) {
    if (values[i] > values[best]) {
      best = i;
    }
  }
  return best;
}
