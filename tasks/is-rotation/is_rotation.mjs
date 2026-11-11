export function isRotation(a, b) {
  if (typeof a !== "string" || typeof b !== "string") {
    throw new TypeError("both arguments must be primitive strings");
  }
  if (a.length > 1000 || b.length > 1000) {
    throw new RangeError("strings are limited to 1000 UTF-16 code units");
  }
  const pointsA = Array.from(a);
  const pointsB = Array.from(b);
  if (pointsA.length !== pointsB.length) {
    return false;
  }
  const n = pointsA.length;
  if (n === 0) {
    return true;
  }
  const doubled = pointsA.concat(pointsA);
  for (let k = 0; k < n; k++) {
    let match = true;
    for (let i = 0; i < n; i++) {
      if (doubled[k + i] !== pointsB[i]) {
        match = false;
        break;
      }
    }
    if (match) {
      return true;
    }
  }
  return false;
}
