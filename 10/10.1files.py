# 1. Дан многострочный файл txt
# а) разбить файл на N(вводится с клавиатуры) файлов построчно
# б) разбить файл на несколько файлов по N строк
n = int(input())
file = open('text.txt', 'r', encoding= 'utf-8')
lines = file.readlines()
for n in range(0, n-1):



print(lines[1])
file.close()
    # for n in range(0, n-1):
    #     new_data = file.write(lines[n])
    #     print(new_data)
    #

