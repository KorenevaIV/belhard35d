# 1. Дан многострочный файл txt
# а) разбить файл на N(вводится с клавиатуры) файлов построчно
# б) разбить файл на несколько файлов по N строк
# n = int(input())
# file = open('text.txt', 'r', encoding= 'utf-8')
# lines = [line.strip() for line in file]
# for line in file:
#     while n >0:
#         new_f = open('file.txt', 'wt')
#         new_f.write(lines[n])
#         n -= 1
#         new_f.close()
#
# print(lines[1])
# file.close()
#
# n = int(input('Enter number: '))
# lines = []  # here will be lists of line[] in quantity 'n'
# with open('text.txt', 'r', encoding='utf-8') as file:
#     while True:
#         line = []  # here will number 'n' of lines from file
#         for _ in range(n):  # iterator will work 'n' times
#             text = file.readline()  # we will read first line
#             text = text.strip()  # then we delete /n from the end of line
#             if text:  # if text is True, it means there are words in this line
#                 line.append(text)  # we add this text into line[], and we will repeat this action fot 'n' times
#             else:
#                 n += 1
#                 continue
#         lines.append(line)
#         if len(line) != n:
#             break


print(lines)
from itertools import zip_longest
from math import ceil

# N = int(input('N: '))
# with open('numbers.txt', 'r', encoding='utf-8') as file:
#     lines = [line.strip() for line in file if line.strip()]
#     count = ceil(len(lines) / N)
#     lines_iter = iter(lines)
#     lines = list(zip_longest(*([lines_iter]*count)))
#
# for i in range(len(lines)):
#     with open(f'{i}.txt', 'w', encoding='utf-8') as file:
#         file.write('\n'.join([line for line in lines[i] if line]))


N = int(input('N: '))
with open('numbers.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file if line.strip()]
    lines_iter = iter(lines)
    lines = list(zip_longest(*([lines_iter]*N)))

for i in range(len(lines)):
    with open(f'{i}.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join([line for line in lines[i] if line]))