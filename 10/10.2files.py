# 2. В файле записано стихотворение. Выведите его на экран, а также
# укажите, каких слов в нем больше: начинающихся на гласную или на
# согласную букву (без учета регистра)?o

with open('text.txt', 'r', encoding= 'utf-8') as file:
    text = file.readlines()

glasn = 0
sogl = 0

for word in text:
    if word[i][0] in 'а,и,е,ё,о,у,ы,э,ю,я':
        glasn += 1
    else:
        sogl += 1


