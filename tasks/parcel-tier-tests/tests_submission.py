import unittest

from implementation import parcel_tier


class IntSubclass(int):
    """An int subclass: the contract requires the exact built-in int."""


class ParcelTierTests(unittest.TestCase):
    def assertRaisesExact(self, exc_type, value):
        with self.assertRaises(exc_type) as caught:
            parcel_tier(value)
        self.assertIs(type(caught.exception), exc_type)

    def test_letter_tier_values(self):
        for grams in (1, 2, 100, 250, 498, 499):
            self.assertEqual(parcel_tier(grams), "letter")

    def test_small_tier_values(self):
        for grams in (500, 501, 750, 1000, 1998, 1999):
            self.assertEqual(parcel_tier(grams), "small")

    def test_medium_tier_values(self):
        for grams in (2000, 2001, 5000, 7500, 9998, 9999):
            self.assertEqual(parcel_tier(grams), "medium")

    def test_large_tier_values(self):
        for grams in (10000, 10001, 20000, 29999, 30000):
            self.assertEqual(parcel_tier(grams), "large")

    def test_lower_bounds_are_inclusive(self):
        self.assertEqual(parcel_tier(1), "letter")
        self.assertEqual(parcel_tier(500), "small")
        self.assertEqual(parcel_tier(2000), "medium")
        self.assertEqual(parcel_tier(10000), "large")

    def test_just_below_each_lower_bound(self):
        self.assertEqual(parcel_tier(499), "letter")
        self.assertEqual(parcel_tier(1999), "small")
        self.assertEqual(parcel_tier(9999), "medium")

    def test_result_is_exact_lowercase_str(self):
        for grams in (1, 500, 2000, 10000):
            result = parcel_tier(grams)
            self.assertIs(type(result), str)
            self.assertEqual(result, result.lower())

    def test_repeat_calls_are_deterministic(self):
        for grams in (1, 499, 500, 1999, 2000, 9999, 10000, 30000):
            self.assertEqual(parcel_tier(grams), parcel_tier(grams))

    def test_bool_raises_type_error(self):
        self.assertRaisesExact(TypeError, True)
        self.assertRaisesExact(TypeError, False)

    def test_float_raises_type_error(self):
        for value in (700.0, 1.0, 499.0, 500.5, -1.5):
            self.assertRaisesExact(TypeError, value)

    def test_type_is_checked_before_range(self):
        # 0.0 is out of range as a number, but the type error must win.
        self.assertRaisesExact(TypeError, 0.0)
        self.assertRaisesExact(TypeError, -1.0)
        self.assertRaisesExact(TypeError, "0")
        self.assertRaisesExact(TypeError, None)

    def test_other_types_raise_type_error(self):
        for value in ("500", "letter", [500], (500,), {"grams": 500}, {500}):
            self.assertRaisesExact(TypeError, value)

    def test_int_subclass_raises_type_error(self):
        self.assertRaisesExact(TypeError, IntSubclass(500))
        self.assertRaisesExact(TypeError, IntSubclass(1))

    def test_below_range_raises_value_error(self):
        for value in (0, -1, -499, -30000):
            self.assertRaisesExact(ValueError, value)

    def test_above_range_raises_value_error(self):
        for value in (30001, 30002, 100000, 10**9):
            self.assertRaisesExact(ValueError, value)

    def test_range_endpoints_are_valid(self):
        self.assertEqual(parcel_tier(1), "letter")
        self.assertEqual(parcel_tier(30000), "large")


if __name__ == "__main__":
    unittest.main()
