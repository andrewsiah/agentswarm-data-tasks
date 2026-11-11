import { types } from "node:util";

export function repeatItems(values, times) {
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
    if (typeof values[i] !== "string") {
      throw new TypeError("every element must be a primitive string");
    }
  }
  if (typeof times !== "number") {
    throw new TypeError("times must be a primitive number");
  }
  if (!Number.isSafeInteger(times) || times < 0 || times > 10) {
    throw new RangeError("times must be a safe integer in [0, 10]");
  }
  const out = new Array(len * times);
  let k = 0;
  for (let i = 0; i < len; i++) {
    const v = values[i];
    for (let j = 0; j < times; j++) {
      out[k] = v;
      k += 1;
    }
  }
  return out;
}
