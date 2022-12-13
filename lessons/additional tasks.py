
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
#
# Программа получает на вход номер месяца - натуральное число N (1<= N <=12)
# и в зависимости от его значения выводит количество дней в месяце. Будем считать,
# что год невисокосный. При решении конечно же используйте оператор match-case
#
#  Cколько дней в каком месяце
#
# Январь - 31 день
# Февраль - 28 дней
# Март - 31 день
# Апрель - 30 дней
# Май - 31 день
# Июнь - 30 дней
# Июль - 31 день
# Август - 31 день
# Сентябрь - 30 дней
# Октябрь - 31 день
# Ноябрь - 30 дней
# Декабрь - 31 день

# # # # #
# # # # # # Спрашивать данные у пользователя с клавиатуры до тех пор пока он не введет число
# # # # #
# # # # # # while not (number := input('Enter number: ')).isdigit():
# # # # # #     pass
# # # # # # N = 44
# # # # # # 2 4 6 8 10
# # # # # # 12 14 16 18 20
# # # # # # 22 24 26 28 30
# # # # # # 32 34 36 38 40
# # # # # # 42 44
# # # # # #
# # # # # # numbers = [0, 1, 2, 3]
# # # # # # for i in range(1, len(numbers)):
# # # # # #     print(numbers[i])
# # # # #
# # # # # # n = int(input('n: '))
# # # # # # m = int(input('m: '))
# # # # # # k = int(input('k: '))
# # # # # #
# # # # # # while n:
# # # # # #     if k % m == 0:
# # # # # #         print(k)
# # # # # #         n -= 1
# # # # # #         k += m
# # # # # #     else:
# # # # # #         k += 1
# # # # #
# # # # #
# # # # # # print(eval(input()))
# # # # #
# # # # #
# # # # # # n = int(input('n: '))
# # # # # #
# # # # # # for i in range(2, n+1, 10):
# # # # # #     for j in range(i, i+9, 2):
# # # # # #         if j <= n:
# # # # # #             print(j, end=' ')
# # # # # #         else:
# # # # # #             break
# # # # # #     print()
# # # # # #
# # # # # # c = 0
# # # # # # matrix = []
# # # # # # line = []
# # # # # # for i in range(2, n+1, 2):
# # # # # #     if c < 5:
# # # # # #         line.append(i)
# # # # # #         c += 1
# # # # # #     else:
# # # # # #         c = 1
# # # # # #         matrix.append(line)
# # # # # #         line = [i]
# # # # # #
# # # # # # matrix.append(line)
# # # # # # for line in matrix:
# # # # # #     print(line)
# # # # #
# # # # # # for i in 'qwerty':
# # # # # #     print(f'{i=}')
# # # # # #     for j in range(10):
# # # # # #         print(f'{j=}')
# # # # #
# # # # # # numbers = []
# # # # # # for i in range(10):
# # # # # #     numbers.append(i)
# # # # # #     print(numbers)
# # # # # #
# # # # # # while numbers:
# # # # # #     del numbers[-1]
# # # # # #     print(numbers)
# # # # #
# # # # #
# # # # # def baz():
# # # # #     print('baz')
# # # # #
# # # # #
# # # # # print(__name__)
# # # # # if __name__ == '__main__':
# # # # #     baz()
# # # # # import os
# # # # # from dotenv import load_dotenv
# # # # # os.mkdir('folder')
# # # # #
# # # # # load_dotenv()
# # # # #
# # # # # print(os.getenv('TOKEN'))
# # # # # import os
# # # # # from pathlib import Path
# # # # #
# # # # # BASE_DIR = Path(__file__).resolve().parent
# # # # # print(BASE_DIR / 'mypackage')
# # # # # print(os.path.join(BASE_DIR, 'mypackage'))
# # # #
# # # #
# # # # from datetime import datetime, timedelta
# # # #
# # # # # date = datetime(
# # # # #     year=2022,
# # # # #     month=5,
# # # # #     day=23
# # # # # )
# # # # date2 = datetime.now()
# # # # # print(date)
# # # # # print(date2)
# # # # # print(date2 - date)
# # # # # print(date2 > date)
# # # # # print(date2.timestamp())
# # # # # print(datetime.fromtimestamp(1669967841.145449))
# # # # print(date2.strftime('%d %B %y %H:%M'))
# # # # date_str = '02 December 22 11:01'
# # # # print(datetime.strptime(date_str, '%d %B %y %H:%M'))
# # # # delta = timedelta(days=5, hours=3)
# # # # print(date2 + delta)
# # # # from http import HTTPStatus
# # # # status_code = 301
# # # # if status_code != HTTPStatus.OK:
# # # #     pass
# # #
# # # # from enum import Enum
# # #
# # #
# # # # class Roles(int, Enum):
# # # #     Admin = 5
# # # #     Manager = 3
# # # #     User = 7
# # # #
# # # #
# # # # class User(object):
# # # #
# # # #     def __init__(self, name: str, role_id: int):
# # # #         self.name = name
# # # #         self.role_id = role_id
# # # #
# # # #
# # # # vasya = User('vasya', 3)
# # # # if vasya.role_id == Roles.Admin:
# # # #     pass
# # # # from enum import IntEnum
# # # #
# # # # roles = [('Admin', 2), ('Manager', 1), ('User', 3)]
# # # # Roles = IntEnum('Roles', roles)
# # # # print(3 == Roles.Admin)
# # # from argparse import ArgumentParser
# # #
# # # parser = ArgumentParser()
# # # parser.add_argument(
# # #     '-p',
# # #     '--port',
# # #     help='PORT',
# # #     default='8000'
# # # )
# # # parser.add_argument(
# # #     '-d',
# # #     '--debug',
# # #     action='store_true'
# # # )
# # # args = parser.parse_args()
# # # print(args)
# #
# # import logging
# #
# # logging.basicConfig(
# #     filename='log.log',
# #     filemode='a',
# #     format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
# # )
# #
# # logging.error('user mudak')
# # from itertools import zip_longest
# # from math import ceil
#
# # N = int(input('N: '))
# # with open('numbers.txt', 'r', encoding='utf-8') as file:
# #     lines = [line.strip() for line in file if line.strip()]
# #     count = ceil(len(lines) / N)
# #     lines_iter = iter(lines)
# #     lines = list(zip_longest(*([lines_iter]*count)))
# #
# # for i in range(len(lines)):
# #     with open(f'{i}.txt', 'w', encoding='utf-8') as file:
# #         file.write('\n'.join([line for line in lines[i] if line]))
#
#
# # N = int(input('N: '))
# # with open('numbers.txt', 'r', encoding='utf-8') as file:
# #     lines = [line.strip() for line in file if line.strip()]
# #     lines_iter = iter(lines)
# #     lines = list(zip_longest(*([lines_iter]*N)))
# #
# # for i in range(len(lines)):
# #     with open(f'{i}.txt', 'w', encoding='utf-8') as file:
# #         file.write('\n'.join([line for line in lines[i] if line]))
# # with open('numbers.txt', 'r', encoding='utf-8') as file:
# #     print(file.read())
# #     file.seek(0)
# #     words = file.read().lower().replace('\n', '').split()
# # vowels = 'ёуеэоаыяиюeyuioa'
# # vowels_count = 0
# # consonants_count = 0
# # for word in words:
# #     if word[0] in vowels:
# #         vowels_count += 1
# #     else:
# #         consonants_count += 1
# # if vowels_count > consonants_count:
# #     print('vowels')
# # elif consonants_count > vowels_count:
# #     print('consonants')
# # else:
# #     print('equal')
# # with open('numbers.txt', 'r', encoding='utf-8') as file:
# #     lines = [line.strip() for line in file]
# #     for line in lines:
# #         if line:
# #             word_count = line.count(' ') + 1
# #             letters_count = 0
# #             for symbol in line:
# #                 if symbol.isalpha():
# #                     letters_count += 1
# #         else:
# #             word_count = 0
# #             letters_count = 0
# #         print(f'{word_count=} {letters_count=}')
# from pydantic import BaseModel
#
#
# class Product(BaseModel):
#     article: str
#     title: str
#     description: str = ''
#     price: float
#
#
# with open('products.csv', 'r', encoding='utf-8') as file:
#     headers = file.readline().strip().split(',')
#     products = []
#     invalid_product = []
#     for product in file:
#         values = product.strip().split(',')
#         product = dict(list(zip(headers, values)))
#         if not product['article']:
#             invalid_product.append(product)
#             continue
#         try:
#             product['price'] = float(product['price'])
#         except ValueError:
#             invalid_product.append(product)
#             continue
#         products.append(product)
# with open('invalid_product.csv', 'w', encoding='utf-8') as file:
#     headers = ','.join(headers)
#     for product in invalid_product:
#         values = ','.join(list(product.values()))
#         headers += f'\n{values}'
#     file.write(headers)
#
# products = list(map(lambda x: Product(**x), products))
# print(products)
# from models import User
#
#
# def send_email(user: User):
#     print(f'message send to {user.email}')
#
#
# users = User.all()
# for user in users:
#     send_email(user=user)