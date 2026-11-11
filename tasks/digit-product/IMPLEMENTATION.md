# digit_product — approach

- Validate type first: `type(n) is not int` raises an exact `TypeError`,
  which rejects bool, int subclasses, and every other type.
- Then range: n outside [0, 10**18] raises an exact `ValueError`.
- Multiply decimal digits with exact integer arithmetic (`% 10` / `//= 10`),
  never floats. A 0 digit makes the product 0, so return early; n == 0 is 0.
- No I/O, no mutation, no retained state; Python 3.11+ stdlib only (no imports).
