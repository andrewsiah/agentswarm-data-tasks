
import { types } from 'node:util';

export function commonPrefix(values) {
  // Check that values is a normal array, not a proxy or subclass.
  if (
    types.isProxy(values) ||
    !Array.isArray(values) ||
    Object.getPrototypeOf(values) !== Array.prototype
  ) {
    throw new TypeError('Expected a normal array');
  }

  const length = values.length;

  // Validate every element before checking the array length.
  for (let i = 0; i < length; i++) {
    // Reject sparse arrays.
    if (!Object.hasOwn(values, i)) {
      throw new TypeError('Sparse arrays are not allowed');
    }

    // Accept only primitive strings.
    if (typeof values[i] !== 'string') {
      throw new TypeError('Every element must be a primitive string');
    }
  }

  // Reject empty arrays.
  if (length === 0) {
    throw new RangeError('Array must not be empty');
  }

  // Convert the first string into Unicode code points.
  const first = Array.from(values[0]);

  let prefixLength = first.length;

  // Compare every remaining string.
  for (let i = 1; i < length; i++) {
    const current = Array.from(values[i]);

    let j = 0;

    while (
      j < prefixLength &&
      j < current.length &&
      first[j] === current[j]
    ) {
      j++;
    }

    prefixLength = j;

    if (prefixLength === 0) {
      return '';
    }
  }

  // Construct and return the common prefix.
  let result = '';

  for (let i = 0; i < prefixLength; i++) {
    result += first[i];
  }

  return result;
}
