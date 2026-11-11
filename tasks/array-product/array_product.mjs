// arrayProduct(values): exact product of the integers of a dense normal
// Array, guarded by the safe-integer limit. See SPEC.md.
//
// values must be a dense normal Array: prototype exactly Array.prototype,
// not a Proxy (checked with types.isProxy from node:util, which also
// catches revoked proxies), and every index an own property. Subclasses,
// altered prototypes, non-arrays and holes raise TypeError. Every element
// must be a primitive number; all element types are validated before any
// value check. Then every element must be an integer with absolute value
// at most 1e9, otherwise RangeError. The result is the exact mathematical
// product (computed with BigInt so no intermediate rounding can occur);
// if its absolute value exceeds Number.MAX_SAFE_INTEGER, RangeError.
// Only the final product counts, and the result is never -0. The input is
// only ever read by index: no mutation, no shadowed methods, no iterator.

import { types } from "node:util";

const MAX_ABS_ELEMENT = 1e9;
const MAX_SAFE_INTEGER = BigInt(Number.MAX_SAFE_INTEGER);

export function arrayProduct(values) {
  if (types.isProxy(values)) {
    throw new TypeError("values must be a normal Array, not a Proxy");
  }
  if (!Array.isArray(values)) {
    throw new TypeError("values must be an Array");
  }
  if (Object.getPrototypeOf(values) !== Array.prototype) {
    throw new TypeError("values must have exactly Array.prototype");
  }
  const length = values.length;
  for (let i = 0; i < length; i++) {
    if (!Object.prototype.hasOwnProperty.call(values, i)) {
      throw new TypeError("values must be dense: every index an own property");
    }
  }
  // Validate ALL element types before any value check.
  for (let i = 0; i < length; i++) {
    if (typeof values[i] !== "number") {
      throw new TypeError("every element must be a primitive number");
    }
  }
  for (let i = 0; i < length; i++) {
    const element = values[i];
    if (!Number.isInteger(element) || Math.abs(element) > MAX_ABS_ELEMENT) {
      throw new RangeError(
        "every element must be an integer with absolute value at most 1e9"
      );
    }
  }
  let product = 1n;
  for (let i = 0; i < length; i++) {
    product *= BigInt(values[i]);
    if (product === 0n) {
      break;
    }
  }
  if (product > MAX_SAFE_INTEGER || product < -MAX_SAFE_INTEGER) {
    throw new RangeError("exact product is not a safe integer");
  }
  return Number(product);
}
