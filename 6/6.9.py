# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

persons = {1 : {'name':'Ivan',
                'surname': 'Ivanov',
                'tel': 123456,
                'email': 'iidogcat@mail.ru'
                },
           2 : {'name': 'Petr',
                'surname': 'Petrov',
                'tel': 124587,
                'email': '' },
           3 : {'name': 'Toma',
                'surname': 'Cvetik',
                'tel': 458966,
                'email': 'iicvet@mail.ru'}

}

a = persons.keys()

for i in a:
    print(persons[i].get('email'))




