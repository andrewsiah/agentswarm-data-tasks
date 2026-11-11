import unittest

from implementation import letter_grade


class _IntSubclass(int):
    """An int subclass: spec requires exact built-in int, so this must fail."""

    pass


class LetterGradeBandTests(unittest.TestCase):
    def test_top_score_is_a(self):
        self.assertEqual(letter_grade(100), "A")

    def test_a_band(self):
        for score in (90, 91, 95, 99, 100):
            with self.subTest(score=score):
                self.assertEqual(letter_grade(score), "A")

    def test_ninety_is_a_not_b(self):
        # Lower bound of the A band is inclusive.
        self.assertEqual(letter_grade(90), "A")

    def test_b_band(self):
        for score in (80, 81, 85, 89):
            with self.subTest(score=score):
                self.assertEqual(letter_grade(score), "B")

    def test_eighty_nine_is_b(self):
        self.assertEqual(letter_grade(89), "B")

    def test_c_band(self):
        for score in (70, 71, 75, 79):
            with self.subTest(score=score):
                self.assertEqual(letter_grade(score), "C")

    def test_seventy_nine_is_c_not_b(self):
        # 79 is the top of the C band, not the start of B.
        self.assertEqual(letter_grade(79), "C")

    def test_seventy_is_c_not_d(self):
        # Lower bound of the C band is inclusive.
        self.assertEqual(letter_grade(70), "C")

    def test_d_band(self):
        for score in (60, 61, 64, 65, 69):
            with self.subTest(score=score):
                self.assertEqual(letter_grade(score), "D")

    def test_sixty_is_d_not_f(self):
        # Lower bound of the D band is inclusive.
        self.assertEqual(letter_grade(60), "D")

    def test_f_band(self):
        for score in (0, 1, 30, 58, 59):
            with self.subTest(score=score):
                self.assertEqual(letter_grade(score), "F")

    def test_fifty_nine_is_f(self):
        self.assertEqual(letter_grade(59), "F")

    def test_zero_is_valid_and_is_f(self):
        self.assertEqual(letter_grade(0), "F")

    def test_result_is_exact_one_char_uppercase_str(self):
        for score in (0, 42, 60, 70, 80, 90, 100):
            with self.subTest(score=score):
                result = letter_grade(score)
                self.assertIs(type(result), str)
                self.assertEqual(len(result), 1)
                self.assertIn(result, ("A", "B", "C", "D", "F"))
                self.assertEqual(result, result.upper())

    def test_no_e_grade_anywhere(self):
        for score in range(0, 101):
            with self.subTest(score=score):
                self.assertNotEqual(letter_grade(score), "E")


class LetterGradeTypeTests(unittest.TestCase):
    def test_bool_raises_type_error(self):
        for value in (True, False):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    letter_grade(value)

    def test_float_raises_type_error(self):
        for value in (85.0, 90.0, 0.0, 59.5):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    letter_grade(value)

    def test_negative_float_raises_type_error_not_value_error(self):
        # Type is checked before range, so -1.0 is a TypeError.
        with self.assertRaises(TypeError):
            letter_grade(-1.0)

    def test_int_subclass_raises_type_error(self):
        with self.assertRaises(TypeError):
            letter_grade(_IntSubclass(90))

    def test_string_raises_type_error(self):
        for value in ("90", "A", ""):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    letter_grade(value)

    def test_none_raises_type_error(self):
        with self.assertRaises(TypeError):
            letter_grade(None)

    def test_containers_raise_type_error(self):
        for value in ([90], (90,), {90}, {"score": 90}):
            with self.subTest(value=repr(value)):
                with self.assertRaises(TypeError):
                    letter_grade(value)


class LetterGradeRangeTests(unittest.TestCase):
    def test_above_100_raises_value_error(self):
        for value in (101, 102, 1000):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    letter_grade(value)

    def test_101_raises_value_error(self):
        with self.assertRaises(ValueError):
            letter_grade(101)

    def test_below_zero_raises_value_error(self):
        for value in (-1, -2, -100):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    letter_grade(value)

    def test_minus_one_raises_value_error(self):
        with self.assertRaises(ValueError):
            letter_grade(-1)

    def test_repeated_calls_are_deterministic(self):
        for score in (0, 59, 60, 75, 88, 90, 100):
            with self.subTest(score=score):
                self.assertEqual(letter_grade(score), letter_grade(score))


if __name__ == "__main__":
    unittest.main()
