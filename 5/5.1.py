#вывести первые n чисел кратные  m  и больше k
n = int(input())  #  сколько нужно вывести цифр
m = int(input())  # кратно этому числу
k = int(input())  # и больше этого числа
#
# lst = []
# c = 0
# i = k
# while c < n:
#     if (i % m == 0):
#         lst.append(i)
#         c += 1
#     i += 1
# print(*lst)
#
# while n:
#     if k%m == 0:
#         print(k)
#         n-=1
#     k += 1
while n:
    if k % m == 0:
        print(k)
        n -= 1
        k += m
    else:
        k += 1
