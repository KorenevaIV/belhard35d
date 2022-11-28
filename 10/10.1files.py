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

with open('text.txt', 'r', encoding= 'utf-8') as file:
    lines = [line.strip() for line in file if line.strip()]

n = int(input('Enter number: '))


print(lines)