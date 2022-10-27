import string

from password import Password

class PasswordValidatorOne:
    def validate(self, passwordValue: string) -> bool:
        password = Password(passwordValue)
        return len(password.__str__()) > 8 \
               and password.getUpperCaseLetterCount() >= 1 \
               and password.getLowerCaseLetterCount() >= 1 \
               and password.getNumbersCount() >= 1 \
               and password.hasUnderscore()