import unittest

from implementation import parking_fee


class IntSubclass(int):
    """An int subclass: not the exact built-in int type."""


class ParkingFeeTierTests(unittest.TestCase):
    def test_zero_minutes_is_free(self):
        self.assertEqual(parking_fee(0), 0)

    def test_grace_period_is_free_through_fifteen(self):
        for minutes in (1, 7, 14, 15):
            with self.subTest(minutes=minutes):
                self.assertEqual(parking_fee(minutes), 0)

    def test_first_paid_tier_boundaries(self):
        # 16 is the first paying minute; the tier runs through 60.
        for minutes in (16, 17, 30, 59, 60):
            with self.subTest(minutes=minutes):
                self.assertEqual(parking_fee(minutes), 4)

    def test_second_tier_boundaries(self):
        # 61 enters the second tier; it runs through 180.
        for minutes in (61, 62, 120, 179, 180):
            with self.subTest(minutes=minutes):
                self.assertEqual(parking_fee(minutes), 10)

    def test_top_tier_boundaries(self):
        # 181 enters the top tier; it runs through the 1440 maximum.
        for minutes in (181, 182, 720, 1439, 1440):
            with self.subTest(minutes=minutes):
                self.assertEqual(parking_fee(minutes), 25)

    def test_fee_is_exact_int(self):
        for minutes in (0, 16, 61, 181, 1440):
            with self.subTest(minutes=minutes):
                self.assertIs(type(parking_fee(minutes)), int)

    def test_deterministic_repeat_calls(self):
        for _ in range(3):
            self.assertEqual(parking_fee(45), 4)


class ParkingFeeTypeTests(unittest.TestCase):
    def test_bool_rejected(self):
        for value in (True, False):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    parking_fee(value)

    def test_int_subclass_rejected(self):
        with self.assertRaises(TypeError):
            parking_fee(IntSubclass(30))

    def test_float_rejected(self):
        for value in (30.0, 0.0, 15.5, 1440.0):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    parking_fee(value)

    def test_type_checked_before_range(self):
        # -1.0 is out of range AND the wrong type; the type error wins.
        with self.assertRaises(TypeError):
            parking_fee(-1.0)
        with self.assertRaises(TypeError):
            parking_fee(2000.5)

    def test_string_none_and_containers_rejected(self):
        for value in ("30", "", None, [30], (30,), {30}, {"minutes": 30}):
            with self.subTest(value=repr(value)):
                with self.assertRaises(TypeError):
                    parking_fee(value)


class ParkingFeeRangeTests(unittest.TestCase):
    def test_negative_minutes_rejected(self):
        for value in (-1, -15, -1440):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parking_fee(value)

    def test_above_maximum_rejected(self):
        for value in (1441, 1442, 2880):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parking_fee(value)

    def test_maximum_is_valid(self):
        self.assertEqual(parking_fee(1440), 25)


if __name__ == "__main__":
    unittest.main()
