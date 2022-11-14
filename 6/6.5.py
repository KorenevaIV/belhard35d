# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза
import dis

list1 = [1, 2, 3, 4, 5]
for i in range(0, len(list1)):
    num = list1.pop(-1)
    print(num, end=' ')
