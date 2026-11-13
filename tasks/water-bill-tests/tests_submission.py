import unittest
from implementation import water_bill


class WaterBillTests(unittest.TestCase):

    def test_zero_units(self):
        self.assertEqual(water_bill(0), 5)

    def test_one_unit(self):
        self.assertEqual(water_bill(1), 7)

    def test_first_tier(self):
        for units in range(2, 11):
            with self.subTest(units=units):
                self.assertEqual(water_bill(units), 5 + 2 * units)

    def test_tier_boundary(self):
        self.assertEqual(water_bill(9), 23)
        self.assertEqual(water_bill(10), 25)
        self.assertEqual(water_bill(11), 28)
        self.assertEqual(water_bill(12), 31)

    def test_second_tier(self):
        for units in [15, 20, 50, 100, 500, 999, 1000]:
            with self.subTest(units=units):
                self.assertEqual(water_bill(units), 25 + 3 * (units - 10))

    def test_maximum_units(self):
        self.assertEqual(water_bill(1000), 2995)

    def test_negative_units(self):
        for units in [-1, -2, -100, -1000]:
            with self.subTest(units=units):
                with self.assertRaises(ValueError):
                    water_bill(units)

    def test_units_above_limit(self):
        for units in [1001, 1002, 2000]:
            with self.subTest(units=units):
                with self.assertRaises(ValueError):
                    water_bill(units)

    def test_invalid_types(self):
        invalid_values = [
            True, False, 3.0, 1.5, "10", None,
            [], {}, (), set()
        ]

        for value in invalid_values:
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    water_bill(value)

    def test_integer_subclass_rejected(self):
        class CustomInt(int):
            pass

        with self.assertRaises(TypeError):
            water_bill(CustomInt(5))

    def test_type_checked_before_range(self):
        for value in [-1.0, 1001.0]:
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    water_bill(value)

    def test_exact_integer_result(self):
        for units in [0, 1, 10, 11, 20, 1000]:
            with self.subTest(units=units):
                self.assertIs(type(water_bill(units)), int)

    def test_deterministic_results(self):
        for units in [0, 10, 11, 100, 1000]:
            first = water_bill(units)
            second = water_bill(units)
            self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()