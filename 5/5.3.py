# вывести четные числа от 2 до  n по 5 в строку
n = int(input())
a = [i for i in range(1, n+1)]
print(a)
while len(a) > 0:
    print(a[0:5])
    del a[0:5]


