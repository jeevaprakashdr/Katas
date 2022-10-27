import re
import string

class PasswordValidatorOne:
    def validate(self, password: string) -> bool:
        upperCaseLetterCount = len(re.findall(r'[A-Z]', password))
        lowerCaseLetterCount = len(re.findall(r'[a-z]', password))
        numbersCount = len(re.findall(r'[0-9]', password))
        hasUnderscore = '_' in password

        return len(password) > 8 \
                  and upperCaseLetterCount >= 1 \
                  and lowerCaseLetterCount >= 1 \
                  and numbersCount >= 1 \
                  and hasUnderscore