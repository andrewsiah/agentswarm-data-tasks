import unittest

from implementation import speed_fine


class IntSubclass(int):
    pass


class SpeedFineTierTests(unittest.TestCase):
    def test_tolerance_tier_pays_zero(self):
        for over in (0, 1, 3, 5):
            with self.subTest(over=over):
                self.assertEqual(speed_fine(over), 0)

    def test_first_tier_pays_50(self):
        for over in (6, 10, 15, 20):
            with self.subTest(over=over):
                self.assertEqual(speed_fine(over), 50)

    def test_second_tier_pays_150(self):
        for over in (21, 30, 35, 40):
            with self.subTest(over=over):
                self.assertEqual(speed_fine(over), 150)

    def test_third_tier_pays_400(self):
        for over in (41, 100, 150, 200):
            with self.subTest(over=over):
                self.assertEqual(speed_fine(over), 400)

    def test_tier_lower_bounds_are_inclusive(self):
        self.assertEqual(speed_fine(6), 50)
        self.assertEqual(speed_fine(21), 150)
        self.assertEqual(speed_fine(41), 400)

    def test_tier_upper_bounds_stay_in_tier(self):
        self.assertEqual(speed_fine(5), 0)
        self.assertEqual(speed_fine(20), 50)
        self.assertEqual(speed_fine(40), 150)

    def test_result_is_exact_int(self):
        for over in (0, 6, 21, 41, 200):
            with self.subTest(over=over):
                self.assertIs(type(speed_fine(over)), int)


class SpeedFineValidationTests(unittest.TestCase):
    def test_negative_raises_value_error(self):
        for over in (-1, -5, -100):
            with self.subTest(over=over):
                with self.assertRaises(ValueError):
                    speed_fine(over)

    def test_above_max_raises_value_error(self):
        for over in (201, 250, 1000):
            with self.subTest(over=over):
                with self.assertRaises(ValueError):
                    speed_fine(over)

    def test_bool_raises_type_error(self):
        for over in (True, False):
            with self.subTest(over=over):
                with self.assertRaises(TypeError):
                    speed_fine(over)

    def test_float_raises_type_error(self):
        for over in (0.0, 10.0, 200.0):
            with self.subTest(over=over):
                with self.assertRaises(TypeError):
                    speed_fine(over)

    def test_negative_float_raises_type_error_not_value_error(self):
        with self.assertRaises(TypeError):
            speed_fine(-1.0)

    def test_other_types_raise_type_error(self):
        for over in ("10", None, [10], (10,), {"over": 10}):
            with self.subTest(over=over):
                with self.assertRaises(TypeError):
                    speed_fine(over)

    def test_int_subclass_raises_type_error(self):
        with self.assertRaises(TypeError):
            speed_fine(IntSubclass(10))


if __name__ == "__main__":
    unittest.main()
