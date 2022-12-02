# 2. В файле записано стихотворение. Выведите его на экран, а также
# укажите, каких слов в нем больше: начинающихся на гласную или на
# согласную букву (без учета регистра)?o


with open('numbers.txt', 'r', encoding='utf-8') as file:
    print(file.read())
    file.seek(0)
    words = file.read().lower().replace('\n', '').split()
vowels = 'ёуеэоаыяиюeyuioa'
vowels_count = 0
consonants_count = 0
for word in words:
    if word[0] in vowels:
        vowels_count += 1
    else:
        consonants_count += 1
if vowels_count > consonants_count:
    print('vowels')
elif consonants_count > vowels_count:
    print('consonants')
else:
    print('equal')


