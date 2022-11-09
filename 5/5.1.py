#вывести первые n чисел кратные  m  и больше k
n = int(input())  #  сколько нужно вывести цифр
m = int(input())  # кратно этому числу
k = int(input())  # и больше этого числа

lst = []
c = 0
i = 0
while c<n:
    if i%3 == 0 and i>k:
        lst.append(i)
        c += 1
    i += 1
print(*lst)