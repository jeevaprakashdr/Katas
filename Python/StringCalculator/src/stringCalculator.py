class StringCalculator:
    def Add(self, number: str) -> int:
        if number.strip():
            numbers = list(map(int, number.split(",")))
            sum_of_numbers = sum(numbers)
            return sum_of_numbers
        else:
            return 0
