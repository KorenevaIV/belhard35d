# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно


numbers = ['a','b','c', 5, 7, 'g', 8, 'a']
numbers = list(filter(lambda x: isinstance(x, str), numbers))

# numbers = list(filter(lambda x: isinstance(x, (str, int)), numbers))

print(numbers)

lst = [2, 3, 4, 5, 'fghj', True, [], None, 'dfgh', 'fgh']
# var 1
# lst = list(filter(lambda x: isinstance(x, str), lst))
# print(lst)
# var 2
i = 0
while i < len(lst):
    if not isinstance(lst[i], str):
        del lst[i]
    else:
        i += 1
print(lst)