# 1. Написать класс Car
# Конструктор класса принимает атрибуты:
# color: str (цвет)
# count_passenger_seats: int (количество пассажирских мест)
# is_baby_seat: bool (наличие десткого кресла)
# is_busy: bool (определяется внутри конструктора со значением False, не принимается на
# вход)
# 1.1 Написать магический метод __str__ выводящий форматированную строку с информацией
# об автомобиле
# 2. Написать класс Taxi
# Конструктор класса принимает атрибуты:
# cars: list[Car] (список экземпляров класса Car)
# 2.1 Реализовать метод find_car
# На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров,
# наличие ребенка, примечание: количество пассажиров с учетом ребенка если он есть)
# На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и
# свободный (is_busy = False), у автомобиля сменить атрибут is_busy на значение True, если
# подходящего автомобиля нет, метод должен возвращать None

from pydantic import BaseModel
class Car:

    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool, is_busy = False) -> None:
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = is_busy



    def __str__(self):
        return f'''Color: {self.color}. There are {self.count_passenger_seats} seats. 
        Seats for baby {"Yes" if self.is_baby_seat else "No"}, Busy: {"Yes" if self.is_busy else "No"}'''

class Taxi(BaseModel):
    def __init__(self, cars: list[Car]) -> None:
        self.cars = cars

    def find_car(self, count_passengers: int, is_baby: bool):

                return self.is_busy = True



car1 = Car('red', 4, True)
print(car1)

