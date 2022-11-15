# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

users = {1 : {'name':'Ivan',
                'surname': 'Ivanov',
                'tel': 123456,
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
for user in users.values():
    # var 1
    # if 'email' not in user:
    #     print(user['name'])
    # elif user['email'] == '':
    #     print(user['name'])

    # var2
    if not user.get('email'):
        print(user.get('name'))









