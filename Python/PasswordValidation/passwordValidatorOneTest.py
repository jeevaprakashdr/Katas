import unittest

from passwordValidatorOne import PasswordValidatorOne


class PasswordValidatorOneTest(unittest.TestCase):

    def test_password_should_have_more_than_8_characters(self):
        validator = PasswordValidatorOne()
        isValid = validator.validate("Abcd_fgh1")
        self.assertEqual(True, isValid)

    def test_password_should_have_a_upper_case_letter(self):
        validator = PasswordValidatorOne()
        isValid = validator.validate("1bcd_fghI")
        self.assertEqual(True, isValid)

    def test_password_should_have_a_lower_case_letter(self):
        validator = PasswordValidatorOne()
        isValid = validator.validate("1bcdefgH_")
        self.assertEqual(True, isValid)

    def test_password_should_have_a_number(self):
        validator = PasswordValidatorOne()
        isValid = validator.validate("1abcdefgH_")
        self.assertEqual(True, isValid)

    def test_password_should_have_a_underscore(self):
        validator = PasswordValidatorOne()
        isValid = validator.validate("1abcdefgHi_")
        self.assertEqual(True, isValid)

