import unittest

from parameterized import parameterized
from password import Password

class PasswordTest(unittest.TestCase):

    def test_password_init_value_should_not_be_modified(self):
        value = "pass"
        password = Password(value)
        self.assertEqual(value, password.__str__())

    def test_number_of_upperCase_letter_in_password(self):
        password = Password("Pass")
        self.assertEqual(1, password.getUpperCaseLetterCount())

    def test_number_of_lowerCase_letter_in_password(self):
        password = Password("PASs")
        self.assertEqual(1, password.getLowerCaseLetterCount())

    def test_number_of_numbers_in_password(self):
        password = Password("PASs123")
        self.assertEqual(3, password.getNumbersCount())

    @parameterized.expand([
        ["PASs123", False],
        ["PASs123_", True]
   ])
    def test_password_has_underscore(self, passwordValue: str, expected: bool):
        password = Password(passwordValue)
        self.assertEqual(expected, password.hasUnderscore())