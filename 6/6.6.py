# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные
randomlist = [1, 4, 6, 9, 15, 77, 32, 90, 101, 53, 86, 1, 4, 15]


newlist = []
newlist2 = []

for i in randomlist:
    if i % 2 == 0:
        newlist.append(i)
    else:
        newlist2.append(i)

a = newlist + newlist2
print(newlist)
print(newlist2)
print(a)
