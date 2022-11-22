# 3. Написать класс Numbers
# Конструктор класса принимает список чисел numbers: list[int]
# Написать метод average — возвращающий среднее арифметическое между всеми числами
# Написать метод max_count — возвращающий число из списка, которое чаще встречается,
# если таких чисел несколько, вывести среднее арифметическое среди таких чисел

from collections import Counter

class Numbers:

    def __init__(self, numbers: list[int]):
        self.numbers = numbers


    def average(self, numbers):
        average_sum = sum(numbers) / len(numbers)
        return average_sum

    def max_count(self, numbers):
        dict_new = dict(Counter(numbers))


