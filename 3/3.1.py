# Пользовователь вводит предложение, заменить все пробелы на "-"2-мя способами

#способ 1

text = input('Введите текст: ')
text_split = text.split()
print('-'.join(text_split))

# способ 2
text = input('Введите текст: ')
print(text.replace(' ', '-'))



