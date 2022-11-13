# Код Морзе для представления цифр и букв использует тире и точки. Напишите
# функцию для кодирования текстового сообщения в соответствии с кодом Морзе.
# (словари в помощь)

# для Вашего удобства словарь вида "буква: код Морзе" уже готов
morze = {
    'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•',
    'g': '——•', 'h': '••••', 'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
    'm': '——', 'n': '—•', 'o': '———', 'p': '•——•', 'q': '——•—', 'r': '•—•',
    's': '•••', 't': '—', 'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
    'y': '—•——', 'z': '——••'
}
def Morse(s):
    a = ''
    for i in s.lower():
        if i in morze.keys():
            a += morze[i] + ' '
        if i == ' ':
            a += ' / '  # Слова разделяются слэшем
    return a


def get_key(val, morze):  # Функция возвращает ключ словаря по значению
    for key, value in morze.items():
        if val == value:
            return key


def MorseTxt(s):
    a, s = '', s.split()
    for i in s:
        if i in morze.values():
            a += get_key(i, morze)
        if i == '/':
            a += ' '
    return a


a = 'The quick brown fox jumps over the lazy dog'
print(Morse(a))
print(MorseTxt(Morse(a)))