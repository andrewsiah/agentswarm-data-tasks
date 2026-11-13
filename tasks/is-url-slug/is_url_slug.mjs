export function isUrlSlug(text) {
  if (typeof text !== 'string') {
    throw new TypeError('text must be a primitive string');
  }

  if (text.length > 1000) {
    throw new RangeError('text is longer than 1000 characters');
  }

  return /^[a-z0-9]+(-[a-z0-9]+)*$/.test(text);
}