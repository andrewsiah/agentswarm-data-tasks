import unittest

from implementation import ticket_price


class IntSubclass(int):
    pass


class TicketPriceTierTests(unittest.TestCase):
    def test_free_tier_pays_0(self):
        for age in (0, 1, 2, 3):
            with self.subTest(age=age):
                self.assertEqual(ticket_price(age), 0)

    def test_child_tier_pays_5(self):
        for age in (4, 8, 12):
            with self.subTest(age=age):
                self.assertEqual(ticket_price(age), 5)

    def test_adult_tier_pays_12(self):
        for age in (13, 30, 50, 64):
            with self.subTest(age=age):
                self.assertEqual(ticket_price(age), 12)

    def test_senior_tier_pays_7(self):
        for age in (65, 90, 120):
            with self.subTest(age=age):
                self.assertEqual(ticket_price(age), 7)

    def test_tier_lower_bounds_are_inclusive(self):
        self.assertEqual(ticket_price(4), 5)
        self.assertEqual(ticket_price(13), 12)
        self.assertEqual(ticket_price(65), 7)

    def test_tier_upper_bounds_stay_in_tier(self):
        self.assertEqual(ticket_price(3), 0)
        self.assertEqual(ticket_price(12), 5)
        self.assertEqual(ticket_price(64), 12)

    def test_result_is_exact_int(self):
        for age in (0, 4, 13, 65, 120):
            with self.subTest(age=age):
                self.assertIs(type(ticket_price(age)), int)


class TicketPriceValidationTests(unittest.TestCase):
    def test_negative_raises_value_error(self):
        for age in (-1, -5, -100):
            with self.subTest(age=age):
                with self.assertRaises(ValueError):
                    ticket_price(age)

    def test_above_max_raises_value_error(self):
        for age in (121, 150, 1000):
            with self.subTest(age=age):
                with self.assertRaises(ValueError):
                    ticket_price(age)

    def test_bool_raises_type_error(self):
        for age in (True, False):
            with self.subTest(age=age):
                with self.assertRaises(TypeError):
                    ticket_price(age)

    def test_float_raises_type_error(self):
        for age in (0.0, 30.0, 120.0):
            with self.subTest(age=age):
                with self.assertRaises(TypeError):
                    ticket_price(age)

    def test_negative_float_raises_type_error_not_value_error(self):
        with self.assertRaises(TypeError):
            ticket_price(-1.0)

    def test_other_types_raise_type_error(self):
        for age in ("30", None, [30], (30,), {"age": 30}):
            with self.subTest(age=age):
                with self.assertRaises(TypeError):
                    ticket_price(age)

    def test_int_subclass_raises_type_error(self):
        with self.assertRaises(TypeError):
            ticket_price(IntSubclass(30))


if __name__ == "__main__":
    unittest.main()
