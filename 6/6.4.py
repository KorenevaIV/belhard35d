# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно

list = ['a','b','c', 5, 7, 'g', 8, 'a']

# for i in list:
#     if type(i) != str:
#         list.remove(i)
# print(list)

new_list = ', '.join(filter(lambda s: str(s) in list, list))
print(new_list)