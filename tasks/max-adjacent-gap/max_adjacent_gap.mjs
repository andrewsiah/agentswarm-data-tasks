// Return the largest absolute difference between neighbouring elements of a
// dense normal Array of integers, in the given order. values must be a real
// Array (prototype exactly Array.prototype, not a Proxy, no subclass, no
// holes) of primitive numbers; wrong types raise TypeError. Elements that
// are not integers or exceed 1e9 in absolute value raise RangeError. Arrays
// with fewer than two elements return 0. Only index loops are used, so
// shadowed array methods and iterators are never called.
import { types } from "node:util";

export function maxAdjacentGap(values) {
  if (
    types.isProxy(values) ||
    !Array.isArray(values) ||
    Object.getPrototypeOf(values) !== Array.prototype
  ) {
    throw new TypeError("values must be a dense normal Array");
  }
  const length = values.length;
  for (let i = 0; i < length; i += 1) {
    if (!Object.prototype.hasOwnProperty.call(values, i)) {
      throw new TypeError("values must be dense: every index an own property");
    }
  }
  for (let i = 0; i < length; i += 1) {
    if (typeof values[i] !== "number") {
      throw new TypeError("every element must be a primitive number");
    }
  }
  for (let i = 0; i < length; i += 1) {
    const element = values[i];
    if (!Number.isInteger(element) || Math.abs(element) > 1e9) {
      throw new RangeError(
        "every element must be an integer with absolute value at most 1e9",
      );
    }
  }
  let max = 0;
  for (let i = 1; i < length; i += 1) {
    const gap = Math.abs(values[i] - values[i - 1]);
    if (gap > max) {
      max = gap;
    }
  }
  return max;
}
