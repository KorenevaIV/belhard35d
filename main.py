# print('hello world')
# print('hello python')
# print("hello dad")
# print("hello python")
# print("hello dear")

# x = int(input())
# y = int(input())
# print(f'Точка({x = } , {y = })')
#
# num = 5
# if num % 2 == 1:
#     print('odd')
#
# word = 'hello2'
# if word.isalpha():
#     print('word')
# else:
#     print('not word')
# word = input()
# if word.isdigit():
#     word = int(word)
#     print('digit')
# elif word.isalpha():
#     print('word')
#
# a = list(map(int, input().split()))
# print(f'{777 in a}')
#
# if (number := int(input('Введите число: '))) < 10000:
#     print(f'Сумма {number} не превышает лимит, проходите')
# else:
#     print(f'Ого! {number}! Куда вам столько? Мы заберем {number - 10000}')

# if 'walrus' in (word := input()):
#     print('Нашли моржа')
# else:
#     print('Никаких моржей тут нет')

# На вход программе поступает целое число
# Ваша задача сохранить в переменную text  строку Even, если введенное число четное, иначе сохраните строку Odd
# В качестве ответа необходимо вывести переменную text
# Sample Input 1:
# 8
# Sample Output 1:
# Even
# num = int(input())
# text = 'Even' if num % 2 == 0 else 'Odd'
# print(text)


#На вход вашей программе поступает два неравных друг друг целых числа в отдельных строках
# Ваша задача сохранить наименьшее из этих чисел в переменную  minimum, а наибольшее - в maximum
# Использовать нужно, конечно же, тернарный оператор
# В качестве ответа выведите через пробел сперва minimum , а потом maximum
#
# num1 = int(input())
# num2 = int(input())
# maximum = num2 if num1 < num2 else num1
# minimum = num1 if num1 < num2 else num2
# print(minimum, maximum)


#Ваша программа принимает на вход предложение и ваша задача определить является ли оно вопросом?
# Если последний символ предложения это знак ?, то в переменную sentence
# сохраните строку Вопросительное, иначе запишите строку Обычное
# В качестве ответа необходимо вывести переменную sentence
# Sample Input 1:
# hasta la vista baby
# Sample Output 1:
# Обычное
# Sample Input 2:
# Как пройти в библиотеку?
# Sample Output 2:
# Вопросительное
# text = input()
# sentence = 'Вопросительное' if text[-1] == '?' else 'Обычное'
# print(sentence)

# Если расположить рядом два магнита, они начинают взаимодействовать друг с другом.
# При этом одинаковые магнитные полюса (север/север или юг/юг) отталкиваются
# друг от друга, в то время как разные магнитные полюса (север/юг) притягиваются друг к другу.
# Ваша программа получает два значения в разных строках - полярности магнитов, которые могут
# иметь значения либо N ( север) либо S (юг)
# Ваша задача сохранить в переменную experiment строку Притягиваются,
# если магниты имеют разную полярность, в противном случае сохраните строку Отталкиваются
# В качестве ответа необходимо вывести переменную experiment
# a = input()
# b = input()
# experiment = 'Притягиваются' if a!=b else 'Отталкиваются'
# print(experiment)


# программа будет получать на вход целое число - номер курса, и в зависимости от номера выводить следующий текст
#
# если ввели 1, выведите сообщение Совсем еще зеленый студентик
# если ввели 2, выведите сообщение Джун-студент
# если ввели 3, выведите сообщение Мидл-студент
# если ввели 4, выведите сообщение Сеньер-студент
# если ввели 5, выведите сообщение Босс качалки
# при вводе остальных значений, выведите текст Неизвестный курс
# Используйте при решении оператор match-case

# num = int(input())
# match num:
#     case 1:
#         print('Совсем еще зеленый студентик')
#     case 2:
#         print('Джун-студент')
#     case 3:
#         print('Мидл-студент')
#     case 4:
#         print('Сеньер-студент')
#     case 5:
#         print('Босс качалки')
#     case _:
#         print('Неизвестный курс')
# первый вариант:
#
# n = int(input())
# i = 1
# while i <= n:
#     if n % i == 0:
#         print(i, end=' ')
#     i+=1
#
# второй вариант:
#
# n = int(input())
# i = 1
# while i <= n//2:
#     if n % i == 0:
#         print(i, end=' ')
#     i+=1
# print(n)
#
# третий вариант:
#
# n = int(input())
# i = 1
# a = []
# while i ** 2 <= n:
#     if n % i == 0:
#         a.append(i)
#         if i != n // i:
#             a.append(n // i)
#     i += 1
# a.sort()
# print(a)

