# 1. Написать класс Car
# Конструктор класса принимает атрибуты:
# color: str (цвет)
# count_passenger_seats: int (количество пассажирских мест)
# is_baby_seat: bool (наличие десткого кресла)
# is_busy: bool (определяется внутри конструктора со значением False, не принимается на
# вход)
# 1.1 Написать магический метод __str__ выводящий форматированную строку с информацией
# об автомобиле
class Car:

    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool, is_busy = False) -> None:
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = is_busy



    def __str__(self):
        return f'''Color: {self.color}. There are {self.count_passenger_seats} seats. 
        Seats for baby {self.is_baby_seat}, Busy: {self.is_busy}'''

car1 = Car('red', 4, True)
print(car1)