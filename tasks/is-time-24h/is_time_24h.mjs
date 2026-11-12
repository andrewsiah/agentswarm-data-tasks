// Return true exactly when text is a 24-hour HH:MM time string: two ASCII
// digits for the hour (00-23), one ":", and two ASCII digits for the minute
// (00-59). text must be a primitive string; anything else raises TypeError.
// A string longer than 1000 UTF-16 code units raises RangeError.
export function isTime24h(text) {
  if (typeof text !== "string") {
    throw new TypeError("text must be a primitive string");
  }
  if (text.length > 1000) {
    throw new RangeError("text must be at most 1000 UTF-16 code units");
  }
  if (text.length !== 5 || text.charAt(2) !== ":") {
    return false;
  }
  const digit = (index) => {
    const code = text.charCodeAt(index);
    return code >= 48 && code <= 57 ? code - 48 : -1;
  };
  const hourTens = digit(0);
  const hourOnes = digit(1);
  const minuteTens = digit(3);
  const minuteOnes = digit(4);
  if (hourTens < 0 || hourOnes < 0 || minuteTens < 0 || minuteOnes < 0) {
    return false;
  }
  const hour = hourTens * 10 + hourOnes;
  const minute = minuteTens * 10 + minuteOnes;
  return hour <= 23 && minute <= 59;
}
