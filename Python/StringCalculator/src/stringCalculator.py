class StringCalculator:
    def Add(self, number: str) -> int:
        if number.strip():
            return int(number)
        else:
            return 0
