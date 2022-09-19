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

    @parameterized.expand([
        ["1, 2", 3],
        ["2, 3, 10", 15],
        ["3, 4, 1, 6", 14],
    ])
    def test_should_return_sum_of_numbers_for_numbers_string(self, numbers, expected):
        calculator = StringCalculator()
        actual = calculator.Add(numbers)
        self.assertEqual(actual, expected)
