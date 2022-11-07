# Пользователь вводит 3 числа, сказать сколько из них  положительрных и сколько отрицательных
# первый способ на определение положительное или отрицательное
# first_num = input('Первое число: ')
# print(first_num.isdigit())
# second_num = input('Второе число: ')
# print(second_num.isdigit())
# third_num = input('Третье число: ')
# print(third_num.isdigit())

# Дальше случился ступор, как без использование  if  и счетчика посчитать сколько каких чисел.
# Наведи пожалуйста на верное решение
first = int(input())
second = int(input())
third = int(input())
# summ = first + second + third
# print('Число отрицательных чисел: ', summ.count('-'))
# print('Число положительных чисел: ', (3 - summ.count('-')))

print('Положительные: ', (first > 0) + (second > 0) + (third > 0))
print('Отрицательные: ', (first < 0) + (second < 0) + (third < 0))