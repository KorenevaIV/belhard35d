# 2. Написать класс Rectangle
# Конструктор класса принимает координаты точек по диагонали (правая нижняя, верхняя
# левая или левая нижняя, правая верхняя)
# Написать метод perimeter возвращающий периметр получившегося прямоугольника
# Написать метод square возвращающий площадь получившегося прямоугольникаы
# *учесть, что координаты на плоскости могут быть отрицательными
class Rectangle:

    def __init__(self, x1, y1, x2, y2):

        self.width = abs(x1-x2)
        self.length = abs(y1-y2)


    def perimeter(self):
        return 2 * (self.length + self.width)

    def square(self):
        return self.length * self.width


rect = Rectangle()

print(rect.square())
print(rect.perimeter())
