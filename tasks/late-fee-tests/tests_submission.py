import unittest

from implementation import late_fee


class IntSubclass(int):
    pass


class LateFeeTierTests(unittest.TestCase):
    def test_grace_period_pays_zero(self):
        for days in (0, 1, 2):
            with self.subTest(days=days):
                self.assertEqual(late_fee(days), 0)

    def test_first_tier_pays_3(self):
        for days in (3, 5, 7, 9):
            with self.subTest(days=days):
                self.assertEqual(late_fee(days), 3)

    def test_second_tier_pays_8(self):
        for days in (10, 15, 20, 29):
            with self.subTest(days=days):
                self.assertEqual(late_fee(days), 8)

    def test_third_tier_pays_20(self):
        for days in (30, 100, 200, 365):
            with self.subTest(days=days):
                self.assertEqual(late_fee(days), 20)

    def test_tier_lower_bounds_are_inclusive(self):
        self.assertEqual(late_fee(3), 3)
        self.assertEqual(late_fee(10), 8)
        self.assertEqual(late_fee(30), 20)

    def test_tier_upper_bounds_stay_in_tier(self):
        self.assertEqual(late_fee(2), 0)
        self.assertEqual(late_fee(9), 3)
        self.assertEqual(late_fee(29), 8)

    def test_result_is_exact_int(self):
        for days in (0, 3, 10, 30, 365):
            with self.subTest(days=days):
                self.assertIs(type(late_fee(days)), int)


class LateFeeValidationTests(unittest.TestCase):
    def test_negative_raises_value_error(self):
        for days in (-1, -5, -100):
            with self.subTest(days=days):
                with self.assertRaises(ValueError):
                    late_fee(days)

    def test_above_max_raises_value_error(self):
        for days in (366, 400, 1000):
            with self.subTest(days=days):
                with self.assertRaises(ValueError):
                    late_fee(days)

    def test_bool_raises_type_error(self):
        for days in (True, False):
            with self.subTest(days=days):
                with self.assertRaises(TypeError):
                    late_fee(days)

    def test_float_raises_type_error(self):
        for days in (0.0, 5.0, 365.0):
            with self.subTest(days=days):
                with self.assertRaises(TypeError):
                    late_fee(days)

    def test_negative_float_raises_type_error_not_value_error(self):
        with self.assertRaises(TypeError):
            late_fee(-1.0)

    def test_other_types_raise_type_error(self):
        for days in ("5", None, [5], (5,), {"days": 5}):
            with self.subTest(days=days):
                with self.assertRaises(TypeError):
                    late_fee(days)

    def test_int_subclass_raises_type_error(self):
        with self.assertRaises(TypeError):
            late_fee(IntSubclass(5))


if __name__ == "__main__":
    unittest.main()
