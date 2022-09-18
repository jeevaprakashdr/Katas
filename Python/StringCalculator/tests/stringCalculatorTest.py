from unittest import TestCase
from src.stringCalculator import StringCalculator


class StringCalculatorTest(TestCase):
    def test_should_return_zero_for_empty_string(self):
        calculator = StringCalculator()
        actual = calculator.Add(" ")
        self.assertEqual(actual, 0)

    def test_should_return_non_zero_for_number_string(self):
        calculator = StringCalculator()
        actual = calculator.Add("5")
        self.assertEqual(actual, 5)