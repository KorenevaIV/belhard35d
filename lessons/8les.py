
# Написать класс Button, конструктор принимает обязательный атрибут text: str
# И не обязательный атрибут request_contact: bool (по умолчанию False)
# реализовать метод объекта dict() возвращающий словарь в формате
# {'text': self.text, 'request_contact': self.request_contact}

# Написать класс Keyboard, конструктор принимает атрибут keyboard - список списков экземпляров
# Button (обязательна проверка на структуру)
# написать метод serialize возвращающий разметку клавиатуры в виде списка списков словарей
class Button:
    """
    Кнопка для клавиатуры
    """

    def __init__(self, text: str, request_contact: bool = False) -> None:
        self.request_contact = request_contact
        self.text = text

    def dict(self) -> dict:
        return {'text': self.text, 'request_contact': self.request_contact}


class Keyboard:

    def __init__(self, keyboard: list[list[Button]]) -> None:
        if not isinstance(keyboard, list):
            raise ValueError('argument `keyboard` must be list')
        for line in keyboard:
            if not isinstance(line, list):
                raise ValueError
            for button in line:
                if not isinstance(button, Button):
                    raise ValueError
        self.keyboard = keyboard

    def serialize(self) -> list[list[dict]]:
        from copy import deepcopy
        keyboard = deepcopy(self.keyboard)
        for j in range(len(keyboard)):
            for i in range(len(keyboard[j])):
                keyboard[j][i] = keyboard[j][i].dict()
        return keyboard

    def insert(self, keyboard: list[Button]):
        if not isinstance(keyboard, list):
            raise ValueError
        for button in keyboard:
            if not isinstance(button, Button):
                raise ValueError
        self.keyboard.append(keyboard)


buttons = [Button(text=text) for text in ('hello', 'python', 'world')]
buttons = [[buttons[0], buttons[1]], [buttons[2]]]
keyboard = Keyboard(keyboard=buttons)
print(keyboard.serialize())


# def multiply(a: int, b: int) -> int:
#     """Произведение двух чисел
#
#     :param a: Первое число произведения
#     :param b: Второе число произведения
#     :return: Результат произведения
#     """
#     return a * b