# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]
list  = [1,2,3,4,5,6,7]
n = int(input())
# a = int(len(list))

# if n <= a:
#     srez1 = list[0:(a-n)]
#     srez2 = list[-n:]
#     new_list = srez2 + srez1
#     print(new_list)
# else:
#     print('Число n  превышает длину списка.')


def list_offset(lst, n):
    n -= len(lst) * (n // len(lst))
    lst = lst[-n:] + lst[:-n]
    return lst


print(list_offset([1, 2, 3, 4, 5, 6, 7], -9))
