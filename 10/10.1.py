# 1. Написать класс Car
class Car:
    # Конструктор класса принимает атрибуты:
    # color: str (цвет)
    # count_passenger_seats: int (количество пассажирских мест)
    # is_baby_seat: bool (наличие десткого кресла)
    # is_busy: bool (определяется внутри конструктора со значением False, не принимается на
    # вход)
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool) -> None:
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False


    # 1.1 Написать магический метод __str__ выводящий форматированную строку с информацией
    # об автомобиле

    def __str__(self):
        return f'''Color: {self.color}. There are {self.count_passenger_seats} seats. 
        Seats for baby {"Yes" if self.is_baby_seat else "No"}, Busy: {"Yes" if self.is_busy else "No"}'''


# 2. Написать класс Taxi
# Конструктор класса принимает атрибуты:
# cars: list[Car] (список экземпляров класса Car)
class Taxi(Car):
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        super().__init__(color, count_passenger_seats, is_baby_seat)
        self.cars = list[Car]

    # 2.1 Реализовать метод find_car
    # На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров,
    # наличие ребенка, примечание: количество пассажиров с учетом ребенка если он есть)
    # На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и
    # свободный (is_busy = False), у автомобиля сменить атрибут is_busy на значение True, если
    # подходящего автомобиля нет, метод должен возвращать None
    def find_car(self, count_passengers: int, is_baby: bool):
        if count_passengers == self.count_passenger_seats and is_baby == self.is_baby_seat:
            if self.is_busy is False:
                self.is_busy = True
                return self.cars
            else:
                return None



car1 = Car('red', 4, True)
car2 = Car('blue', 5, True)
car3 = Car('black', 5, False)
car4 = Car('white', 4, False)

print(car1)

