import unittest

from implementation import rental_fee


class IntSubclass(int):
    pass


class RentalFeeTierTests(unittest.TestCase):
    def test_first_hour_costs_4(self):
        self.assertEqual(rental_fee(1), 4)

    def test_full_price_tier(self):
        for hours, fee in ((1, 4), (2, 8), (3, 12)):
            with self.subTest(hours=hours):
                self.assertEqual(rental_fee(hours), fee)

    def test_reduced_tier_starts_at_four_hours(self):
        self.assertEqual(rental_fee(4), 14)
        self.assertEqual(rental_fee(5), 16)

    def test_reduced_tier_progression(self):
        for hours, fee in ((6, 18), (7, 20), (8, 22), (9, 24), (10, 26), (11, 28)):
            with self.subTest(hours=hours):
                self.assertEqual(rental_fee(hours), fee)

    def test_just_below_cap(self):
        self.assertEqual(rental_fee(11), 28)

    def test_cap_reached_at_twelve_hours(self):
        self.assertEqual(rental_fee(12), 30)

    def test_cap_stays_flat_above_twelve(self):
        for hours in (13, 20, 24, 48, 71, 72):
            with self.subTest(hours=hours):
                self.assertEqual(rental_fee(hours), 30)

    def test_result_is_exact_int(self):
        for hours in (1, 3, 4, 11, 12, 72):
            with self.subTest(hours=hours):
                self.assertIs(type(rental_fee(hours)), int)


class RentalFeeValidationTests(unittest.TestCase):
    def test_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            rental_fee(0)

    def test_negative_raises_value_error(self):
        for hours in (-1, -3, -72):
            with self.subTest(hours=hours):
                with self.assertRaises(ValueError):
                    rental_fee(hours)

    def test_above_max_raises_value_error(self):
        for hours in (73, 100, 1000):
            with self.subTest(hours=hours):
                with self.assertRaises(ValueError):
                    rental_fee(hours)

    def test_max_boundary_is_valid(self):
        self.assertEqual(rental_fee(72), 30)

    def test_bool_raises_type_error(self):
        for hours in (True, False):
            with self.subTest(hours=hours):
                with self.assertRaises(TypeError):
                    rental_fee(hours)

    def test_float_raises_type_error(self):
        for hours in (1.0, 3.0, 12.5):
            with self.subTest(hours=hours):
                with self.assertRaises(TypeError):
                    rental_fee(hours)

    def test_type_checked_before_range(self):
        with self.assertRaises(TypeError):
            rental_fee(-1.0)
        with self.assertRaises(TypeError):
            rental_fee(100.0)

    def test_other_types_raise_type_error(self):
        for hours in ("3", None, [3], (3,), {"hours": 3}):
            with self.subTest(hours=hours):
                with self.assertRaises(TypeError):
                    rental_fee(hours)

    def test_int_subclass_raises_type_error(self):
        with self.assertRaises(TypeError):
            rental_fee(IntSubclass(3))


if __name__ == "__main__":
    unittest.main()
