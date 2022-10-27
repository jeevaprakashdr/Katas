import re

class Password:

    def __init__(self, value: str):
        self._value = value

    def __str__(self) -> str:
        return self._value

    def getUpperCaseLetterCount(self):
        return len(re.findall(r'[A-Z]', self._value))

    def getLowerCaseLetterCount(self):
        return len(re.findall(r'[a-z]', self._value))

    def getNumbersCount(self):
        return len(re.findall(r'[0-9]', self._value))

    def hasUnderscore(self):
        return '_' in self._value


