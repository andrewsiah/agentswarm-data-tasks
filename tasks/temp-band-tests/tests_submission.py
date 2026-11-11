import unittest

from implementation import temp_band


class IntSubclass(int):
    pass


class StrSubclass(str):
    pass


class FloatSubclass(float):
    pass


def expected_band(celsius):
    if celsius < 0:
        return "freezing"
    if celsius < 10:
        return "cold"
    if celsius < 20:
        return "mild"
    if celsius < 30:
        return "warm"
    return "hot"


class TempBandValueTests(unittest.TestCase):
    def test_range_endpoints_are_valid(self):
        self.assertEqual(temp_band(-100), "freezing")
        self.assertEqual(temp_band(100), "hot")

    def test_freezing_band(self):
        for value in (-100, -99, -50, -2, -1):
            self.assertEqual(temp_band(value), "freezing")

    def test_cold_band(self):
        for value in (0, 1, 5, 8, 9):
            self.assertEqual(temp_band(value), "cold")

    def test_mild_band(self):
        for value in (10, 11, 15, 18, 19):
            self.assertEqual(temp_band(value), "mild")

    def test_warm_band(self):
        for value in (20, 21, 25, 28, 29):
            self.assertEqual(temp_band(value), "warm")

    def test_hot_band(self):
        for value in (30, 31, 50, 99, 100):
            self.assertEqual(temp_band(value), "hot")

    def test_lower_bounds_are_inclusive(self):
        self.assertEqual(temp_band(-1), "freezing")
        self.assertEqual(temp_band(0), "cold")
        self.assertEqual(temp_band(9), "cold")
        self.assertEqual(temp_band(10), "mild")
        self.assertEqual(temp_band(19), "mild")
        self.assertEqual(temp_band(20), "warm")
        self.assertEqual(temp_band(29), "warm")
        self.assertEqual(temp_band(30), "hot")

    def test_full_sweep_matches_spec(self):
        for value in range(-100, 101):
            with self.subTest(celsius=value):
                self.assertEqual(temp_band(value), expected_band(value))

    def test_returns_exact_lowercase_str(self):
        for value in (-100, -1, 0, 10, 20, 30, 100):
            result = temp_band(value)
            self.assertIs(type(result), str)
            self.assertEqual(result, result.lower())

    def test_repeated_calls_are_deterministic(self):
        for value in (-7, 0, 13, 22, 30):
            self.assertEqual(temp_band(value), temp_band(value))


class TempBandTypeTests(unittest.TestCase):
    def test_bool_raises_type_error(self):
        with self.assertRaises(TypeError):
            temp_band(True)
        with self.assertRaises(TypeError):
            temp_band(False)

    def test_float_raises_type_error(self):
        for bad in (0.0, 15.0, -1.5, 100.0):
            with self.assertRaises(TypeError):
                temp_band(bad)

    def test_type_is_checked_before_range(self):
        # -101.0 and 101.0 are out of range numerically, but the type
        # check must fire first, so these raise TypeError, not ValueError.
        with self.assertRaises(TypeError):
            temp_band(-101.0)
        with self.assertRaises(TypeError):
            temp_band(101.0)

    def test_string_and_none_raise_type_error(self):
        for bad in ("0", "cold", "", None):
            with self.assertRaises(TypeError):
                temp_band(bad)

    def test_containers_raise_type_error(self):
        for bad in ([0], (0,), {0: "cold"}, {0}):
            with self.assertRaises(TypeError):
                temp_band(bad)

    def test_subclasses_raise_type_error(self):
        with self.assertRaises(TypeError):
            temp_band(IntSubclass(15))
        with self.assertRaises(TypeError):
            temp_band(StrSubclass("15"))
        with self.assertRaises(TypeError):
            temp_band(FloatSubclass(15.0))


class TempBandRangeTests(unittest.TestCase):
    def test_below_range_raises_value_error(self):
        for bad in (-101, -102, -1000, -(10**20)):
            with self.assertRaises(ValueError):
                temp_band(bad)

    def test_above_range_raises_value_error(self):
        for bad in (101, 102, 1000, 10**20):
            with self.assertRaises(ValueError):
                temp_band(bad)


if __name__ == "__main__":
    unittest.main()
