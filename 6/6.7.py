# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка

# nums = [1, 4, 6, 9, 15, 77, 32, 90, 101, 53, 86, 1, 4, 15]
#
# list = []       #14 индексов от 0 до 13
# for i in range(len(nums)):
#     if i == 0:
#         m = nums[-1] + nums[1]
#         list.append(m)
#     elif i > 0 and i < len(nums)-1:
#         m = nums[i-1] + nums[i+1]
#         list.append(m)
#     elif i == len(nums)-1:
#         m = nums[len(nums)-2] + nums[0]
#         list.append(m)
# print(list)


def sum_neighbor(numbers):
    result = []
    for i in range(len(numbers)):
        if i < len(numbers) - 1:
            result.append(numbers[i-1] + numbers[i+1])
        else:
            result.append(numbers[i-1] + numbers[0])
    return result


numbers = [1, 2, 3, 4, 5, 6, 7]
print(sum_neighbor(numbers))