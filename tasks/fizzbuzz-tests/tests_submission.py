import unittest

from implementation import fizzbuzz


class FizzBuzzTypeTests(unittest.TestCase):
    def test_bool_is_not_accepted(self):
        with self.assertRaises(TypeError):
            fizzbuzz(True)
        with self.assertRaises(TypeError):
            fizzbuzz(False)

    def test_float_is_not_accepted_even_when_integral_or_negative(self):
        with self.assertRaises(TypeError):
            fizzbuzz(3.0)
        with self.assertRaises(TypeError):
            fizzbuzz(-3.0)

    def test_other_non_int_types_are_rejected(self):
        for value in (None, "3", [3], (3,), {3}, frozenset((3,)), 3j):
            with self.subTest(value=value), self.assertRaises(TypeError):
                fizzbuzz(value)

    def test_int_subclass_is_rejected(self):
        class IntSubclass(int):
            pass

        with self.assertRaises(TypeError):
            fizzbuzz(IntSubclass(3))


class FizzBuzzRangeTests(unittest.TestCase):
    def test_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            fizzbuzz(0)

    def test_negative_integers_raise_value_error(self):
        for value in (-1, -3, -5, -15, -(10**100)):
            with self.subTest(value=value), self.assertRaises(ValueError):
                fizzbuzz(value)

    def test_type_is_checked_before_range(self):
        with self.assertRaises(TypeError):
            fizzbuzz(-3.0)


class FizzBuzzValueTests(unittest.TestCase):
    def test_plain_numbers_return_exact_decimal_strings(self):
        for value in (1, 2, 4, 7, 8, 11, 98, 10**100 - 2):
            with self.subTest(value=value):
                self.assertIs(type(fizzbuzz(value)), str)
                self.assertEqual(fizzbuzz(value), str(value))

    def test_multiples_of_three_return_fizz(self):
        for value in (3, 6, 9, 12, 99, 3 * (10**100 + 1)):
            with self.subTest(value=value):
                self.assertEqual(fizzbuzz(value), "Fizz")

    def test_multiples_of_five_return_buzz(self):
        for value in (5, 10, 20, 35, 100, 5 * 10**100):
            with self.subTest(value=value):
                self.assertEqual(fizzbuzz(value), "Buzz")

    def test_multiples_of_fifteen_return_fizzbuzz(self):
        for value in (15, 30, 45, 150, 15 * 10**100):
            with self.subTest(value=value):
                self.assertEqual(fizzbuzz(value), "FizzBuzz")

    def test_words_are_exact_and_have_no_extra_whitespace(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertNotEqual(fizzbuzz(15), "Fizz Buzz")

    def test_calls_are_deterministic(self):
        self.assertEqual(fizzbuzz(98), fizzbuzz(98))
        self.assertEqual(fizzbuzz(15), fizzbuzz(15))

if __name__ == "__main__":
    unittest.main()
