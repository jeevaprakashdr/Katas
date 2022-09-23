class StringCalculator:
    def __init__(self):
        self.__separators = list([',', '\n'])

    def Add(self, numbers: str) -> int:
        if self.__IsEmptyString(numbers):
            return 0
        elif len(numbers.strip()) == 1:
            return int(numbers)
        else:
            numbers = self.__GetNumberCollection(numbers)
            numbers = self.__filterNumbers(numbers)
            self.__CheckNegativeNumbers(numbers)
            return sum(numbers)

    def __GetNumberCollection(self, numbers: str) -> list:
        collection = list([])
        for separator in self.__separators:
            if numbers.__contains__(separator):
                collection = numbers.split(separator)
            else:
                collection = collection

        return self.__MapToIntegerCollection(collection)

    def __IsEmptyString(self, value: str) -> bool:
        return not value.strip()

    def __MapToIntegerCollection(self, collection: list) -> list:
        return list(map(int, collection))

    def __CheckNegativeNumbers(self, collection: list):
        items = list(filter(lambda item: item < 0, collection))
        if len(items) > 0:
            raise RuntimeError("negatives not allowed")

    def __filterNumbers(self, collection: list) -> list:
        return list(filter(lambda item: item < 1000, collection))