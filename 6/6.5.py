# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

numbers = [1, 2, 3, 4, 5]
# for i in range(0, len(list1)):
#     num = list1.pop(-1)
#     print(num, end=' ')


def newlist(text):
    output = []
    for i in range(len(text)-1, -1, -1):
        output.append(text[i])
    return output


print(newlist(numbers))
