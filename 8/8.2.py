# 2. Написать класс Rectangle
# Конструктор класса принимает координаты точек по диагонали (правая нижняя, верхняя
# левая или левая нижняя, правая верхняя)
# Написать метод perimeter возвращающий периметр получившегося прямоугольника
# Написать метод square возвращающий площадь получившегося прямоугольникаы
# *учесть, что координаты на плоскости могут быть отрицательными
class Rectangle:

    def __init__(self, coord: (int, int), coord2:(int, int)):
        self.coord = coord
        self.coord2 = coord2


    def get_length(self, ):
        return self.a

    def get_width(self):
        return self.b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b


rect = Rectangle(3, 4)
print(rect.get_length())
print(rect.get_width())
print(rect.square())
print(rect.perimeter())
