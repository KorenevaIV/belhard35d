# 1. Написать класс Student
# Конструктор класса принимает аргументы: first_name: str, group: int, marks: list[int]
# Написать метод __str__ возвращающая форматированную строку с данными об студенте
# Написать функцию (не метод) student_sort принимающая список студентов: students:
# list[Student] и возвращающая список студентов отсортированный по имени
class Student:
    def __init__(self, first_name: str, group: int,marks: list[int]):
        self.first_name = first_name
        self.group = group
        self.marks = marks

    def __str__(self):
        data_about_student = f'{self.first_name} {self.group} {self.marks}'
        return data_about_student
