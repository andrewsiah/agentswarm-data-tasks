// Validate a dotted-decimal IPv4 address. Node 22 standard library only.

const MAX_LENGTH = 1000;

export function isIpv4(text) {
  // typeof is "string" only for primitive strings; boxed String objects
  // (and subclasses), numbers, null and undefined all fail this check.
  if (typeof text !== "string") {
    throw new TypeError("text must be a primitive string");
  }
  if (text.length > MAX_LENGTH) {
    throw new RangeError("text must be at most 1000 UTF-16 code units");
  }

  const parts = text.split(".");
  if (parts.length !== 4) {
    return false;
  }

  for (const part of parts) {
    const len = part.length;
    if (len < 1 || len > 3) {
      return false;
    }
    // Only ASCII digits 0-9 are accepted.
    for (let i = 0; i < len; i++) {
      const c = part.charCodeAt(i);
      if (c < 48 || c > 57) {
        return false;
      }
    }
    // No leading zero unless the part is exactly "0".
    if (len > 1 && part.charCodeAt(0) === 48) {
      return false;
    }
    if (Number(part) > 255) {
      return false;
    }
  }

  return true;
}