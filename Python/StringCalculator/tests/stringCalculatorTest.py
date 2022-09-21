import unittest
from parameterized import parameterized
from src.stringCalculator import StringCalculator


class StringCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = StringCalculator()
    @parameterized.expand([
        [""],
        [" "],
        ["  "],
    ])
    def test_should_return_zero_for_empty_string(self, number):
        actual = self.calculator.Add(number)
        self.assertEqual(actual, 0)

    def test_should_return_non_zero_for_number_string(self):
        actual = self.calculator.Add("5")
        self.assertEqual(actual, 5)

    @parameterized.expand([
        ["1,2", 3],
        ["2,3,10", 15],
        ["3,4,1,6", 14],
    ])
    def test_should_return_sum_of_numbers_for_numbers_string(self, numbers, expected):
        actual = self.calculator.Add(numbers)
        self.assertEqual(actual, expected)

    @parameterized.expand([
        ["1\n2",3],
    ])
    def test_should_return_sum_of_numbers_for_numbers_string_seperated_by_newline(self, numbers, expected):
        actual = self.calculator.Add(numbers)
        self.assertEqual(actual, expected)

    @parameterized.expand([
        ["1, -2, -3"],
    ])
    def test_should_throw_exception_for_negative_numbers_in_string(self, number_string):
        with self.assertRaises(RuntimeError, msg="negatives not allowed"):
            self.calculator.Add(number_string)


