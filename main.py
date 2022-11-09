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
num = int(input())
text = 'Even' if num % 2 else '0dd'
print(text)


