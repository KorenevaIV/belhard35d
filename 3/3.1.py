# Пользовователь вводит предложение, заменить все пробелы на "-"2-мя способами
text = input('Введите текст: ')
text_split = text.split()
print('-'.join(text_split))

