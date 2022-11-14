# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны
dict = {'Belarus': ['Minsk', 'Grodno', 'Brest'],
        'Poland': ['Gdansk', 'Belostok', 'Warsaw'],
        'Ukrain': ['Lviv', 'Kiev', 'Rovno']
        }

txt = input('Enter name of the city: ')
for key in dict.keys():
        if txt in dict[key]:
            print(key)


