// rangeSpan(values): largest minus smallest integer of a dense nonempty
// normal Array. See SPEC.md.
//
// values must be a dense normal Array: prototype exactly Array.prototype,
// not a Proxy (checked with types.isProxy from node:util, which also
// catches revoked proxies), and every index an own property. Subclasses,
// altered prototypes, non-arrays and holes raise TypeError. Every element
// must be a primitive number; all element types are validated before any
// value check. Then an empty array raises RangeError, and every element
// must be an integer with absolute value at most 1e15, otherwise
// RangeError. Returns max - min as a primitive number, never -0. The
// input is only ever read by index: no mutation, no shadowed methods, no
// input iterator, so frozen arrays work.

import { types } from "node:util";

const MAX_ABS_ELEMENT = 1e15;

export function rangeSpan(values) {
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
  if (length === 0) {
    throw new RangeError("values must not be empty");
  }
  for (let i = 0; i < length; i++) {
    const element = values[i];
    if (!Number.isInteger(element) || Math.abs(element) > MAX_ABS_ELEMENT) {
      throw new RangeError(
        "every element must be an integer with absolute value at most 1e15"
      );
    }
  }
  let min = values[0];
  let max = values[0];
  for (let i = 1; i < length; i++) {
    const element = values[i];
    if (element < min) {
      min = element;
    }
    if (element > max) {
      max = element;
    }
  }
  const span = max - min;
  // Normalize a possible -0 result to 0.
  return span === 0 ? 0 : span;
}
