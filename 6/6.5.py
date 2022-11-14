# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

numbers = [1, 2, 3, 4, 5]


# def newlist(text):
#     output = []
#     for i in range(len(text)-1, -1, -1):
#         output.append(text[i])
#     return output
#
#
# print(newlist(numbers))

def newlist(num):
    if len(num) == 0:
        print('')
    else:
        print(num[-1], end=' ')
        newlist(num[:-1])

newlist(numbers)
