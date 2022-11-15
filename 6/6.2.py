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
# def Morse(s):
#     global morze
#     a = ''
#     for i in s.lower():
#         if i in morze.keys():
#             a += morze[i] + ' '
#         if i == ' ':
#             a += ' / '  # Слова разделяются слэшем
#     return a
#
#
# a = 'THello world how are you'
# print(Morse(a))
#
#
# #как назад вернуть в текст
# def get_key(val, morze):  # Функция возвращает ключ словаря по значению
#     for key, value in morze.items():
#         if val == value:
#             return key
#
# def MorseTxt(s):
#     a, s = '', s.split()
#     for i in s:
#         if i in morze.values():
#             a += get_key(i, morze)
#         if i == '/':
#             a += ' '
#     return a
#
# print(MorseTxt(Morse(a)))

def text_to_morse(text):
    global morse
    result = ''
    text = text.lower()
    for i in text:
        if i in morse:
            result += morse[i] + ' '
        elif i == ' ':
            result += '  '
    return result


def morse_to_text(morse_text):
    global morse
    morse_text = morse_text.replace('   ', ' | ').split()
    text = ''
    for i in morse_text:
        if i == '|':
            text += ' '
        else:
            for key, val in morse.items():
                if i == val:
                    text += key
                    break
    return text


print(morse_to_text(text_to_morse(text='Hello world')))

