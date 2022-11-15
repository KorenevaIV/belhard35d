# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные
randomlist = [1, 4, 6, 9, 15, 77, 32, 90, 101, 53, 86, 1, 4, 15]

list = []
for i in randomlist:
    if i % 2 == 0:
        list.insert(0, i)
    else:
        list.append(i)

print(list)


numbers = [2, 6, 3, 4, 3, 3, 5, 6, 8, 2, 34, 6, 4]


def my_sort(numbers):
    # result = []
    # for i in range(len(numbers)):
    #     if numbers[i] % 2:
    #         result.append(numbers[i])
    #     else:
    #         result.insert(0, numbers[i])
    # return result
    # for i in range(len(numbers)):
    #     if numbers[i] % 2 == 0:
    #         numbers.insert(0, numbers.pop(i))
    # return numbers
    numbers = list(filter(lambda x: not x % 2, numbers)) + list(filter(lambda x: x % 2, numbers))
    return numbers


print(my_sort(numbers))
