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


countries = {
    'телемелитрямдия': ['нарния'],
    'россия': ['москва', 'питер'],
    'беларусь': ['минск', 'могилев', 'гомель']
}


def find_country(city):
    global countries
    for country, cities in countries.items():
        if city.lower() in cities:
            return country
    return 'страна не найдена'


print(find_country('могилев'))