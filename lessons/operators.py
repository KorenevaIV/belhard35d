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

#тернарный операвтор
#
# num = 5
# is_even = 'nechet' if num %2 else 'chet'
#
# if num % 2:
#     is_even = False
# else:
#     is_even = True
#
# text = 'hello'
# res = 'slovo' if  text.isalpha() else 'chislo' if text.isdigit() else 'not word'

# циклы  for and while

# for i in range(1, 10, 2): #1 3 5 7 9
#     i**=2
#     print(i)
# print(i)

numbers = [2, 5, 3, 6, 9, 5 ]
# итерация по индексам
# for i in range(len(numbers)):
#      print(numbers[i])
# работа с каждым числом по отдельностиб итерация по элементам
#for num in numbers:
#    print(num)

 # к строкам спискам кортежам по индексам
# for i in enumerate(numbers):
#     print(i)

# for i, val in enumerate(numbers):
#     print(i, val)

# вводится текст
text = input('текст: ').split()
for i in text:
    if len(i) > 5:
        print(i)




