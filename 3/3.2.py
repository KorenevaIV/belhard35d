# Пользователь вводит три числа, найти среднее арифмитическое с точностью 3

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
third_number = int(input('Введите третье число: '))
average = (first_number + second_number + third_number) / 3
print(round(average, 3))

