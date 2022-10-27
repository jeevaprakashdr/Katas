import re
import string

class PasswordValidator:
    def validate(self, password: string) -> bool:
        capitalLettersCount = len(re.findall(r'[A-Z]', password))
        return len(password) > 8 and capitalLettersCount >= 1
