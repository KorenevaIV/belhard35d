# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные
randomlist = [1, 4, 6, 9, 15, 77, 32, 90, 101, 53, 86, 1, 4, 15]

list = []
for i in randomlist:
    if i %2 == 0:
        list.insert(0, i)
    else:
        list.append(i)


print(list)

