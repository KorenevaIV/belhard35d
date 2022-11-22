# 1. Написать класс Student
# Конструктор класса принимает аргументы: first_name: str, group: int, marks: list[int]
# Написать метод __str__ возвращающая форматированную строку с данными об студенте
# Написать функцию (не метод) student_sort принимающая список студентов: students:
# list[Student] и возвращающая список студентов отсортированный по имени
class Student:
    def __init__(self, first_name: str, group: int, marks: list[int]) -> None:
        self.first_name = first_name
        self.group = group
        self.marks = marks

    def __str__(self) -> str:
         return f'Name: {self.first_name} Group: {self.group} Marks: {self.marks}'


user = Student('Alex', 45, [1, 2, 3])
user2 = Student('Eva', 44, [4, 5, 6])
user3 = Student('Ivan', 45, [5, 4, 3])
students = [user, user3, user2]


# def student_sort(students) -> list:
#     return sorted(students, key = lambda student: student.first_name)

def student_sort(students: list[Student]) -> list[Student]:
    return sorted(students, key=lambda student: student.first_name)

students = student_sort(students)
for student in students:
    print(student)