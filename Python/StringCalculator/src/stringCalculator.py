class StringCalculator:
    def __init__(self):
        self.__separators = list([',', '\n'])

    def Add(self, numbers: str) -> int:
        if self.__IsEmptyString(numbers):
            return 0
        else:
            numbers = self.__GetNumberCollection(numbers)
            sum_of_numbers = sum(numbers)
            return sum_of_numbers

    def __GetNumberCollection(self, numbers: str) -> list:
        collection = list([])
        if len(numbers) == 1:
            collection.extend(numbers)
            return self.__MapToIntegerCollection(collection)

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
