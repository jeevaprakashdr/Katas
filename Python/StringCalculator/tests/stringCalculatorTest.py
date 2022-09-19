import unittest
from parameterized import parameterized
from src.stringCalculator import StringCalculator


class StringCalculatorTest(unittest.TestCase):

    @parameterized.expand([
        [""],
        [" "],
        ["  "],
    ])
    def test_should_return_zero_for_empty_string(self, number):
        calculator = StringCalculator()
        actual = calculator.Add(number)
        self.assertEqual(actual, 0)

    def test_should_return_non_zero_for_number_string(self):
        calculator = StringCalculator()
        actual = calculator.Add("5")
        self.assertEqual(actual, 5)