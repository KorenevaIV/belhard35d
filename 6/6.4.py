# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно


numbers = ['a','b','c', 5, 7, 'g', 8, 'a']
numbers = list(filter(lambda x: isinstance(x, str), numbers))
# numbers = [i for i in numbers if isinstance(i, str)]
# #
#
print(numbers)


