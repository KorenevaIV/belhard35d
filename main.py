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

if (number := int(input('Введите число: '))) < 10000:
    print(f'Сумма {number} не превышает лимит, проходите')
else:
    print(f'Ого! {number}! Куда вам столько? Мы заберем {number - 10000}')
