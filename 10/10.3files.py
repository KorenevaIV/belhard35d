3. Дан файл с текстом, необходимо в проанализировать файл и сказать
сколько слов и букв в каждой строке
with open('numbers.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file]
    for line in lines:
        if line:
            word_count = line.count(' ') + 1
            letters_count = 0
            for symbol in line:
                if symbol.isalpha():
                    letters_count += 1
        else:
            word_count = 0
            letters_count = 0
        print(f'{word_count=} {letters_count=}')