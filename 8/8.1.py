# 1. Написать класс Student
# Конструктор класса принимает аргументы: first_name: str, group: int, marks: list[int]
# Написать метод __str__ возвращающая форматированную строку с данными об студенте
# Написать функцию (не метод) student_sort принимающая список студентов: students:
# list[Student] и возвращающая список студентов отсортированный по имени
class Student:
    def __init__(self, first_name: str, group: int, marks: list[int]):
        self.first_name = first_name
        self.group = group
        self.marks = marks

    def __str__(self):
        data_about_student = f'{self.first_name} {self.group} {self.marks}'
        return data_about_student

user = Student('Alex', 45, [1, 2, 3])
user2 = Student('Eva', 44, [4, 5, 6])
user3 = Student('Ivan', 45, [5, 4, 3])



def student_sort(self, list[Student]) -> list:
    sorted(list, key = self.first_name)


print(student_sort(list[Student]))
