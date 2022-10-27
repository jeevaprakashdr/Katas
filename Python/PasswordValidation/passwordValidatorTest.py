import unittest

from passwordValidator import PasswordValidator


class PasswordValidatorTest(unittest.TestCase):

    def test_password_should_have_more_than_8_characters(self):
        validator = PasswordValidator()
        isValid = validator.validate("Abcdefghi")
        self.assertEqual(True, isValid)

    def test_password_should_have_a_capital_letter(self):
        validator = PasswordValidator()
        isValid = validator.validate("Abcdefghi")
        self.assertEqual(True, isValid)
