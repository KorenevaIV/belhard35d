
# print(bin(10))
# print(bin(14))
# print(bin(10 ^ 14))
# print(~123)
# print(bin(14))
# print(bin(14 >> 2))


# аннотация типов при определении переменных и изменении типа данных
# a: int = int(input())
# a += 1
# a: str = str(a)
#
# расширенная типизация до python 3.10
# from typing import List, Tuple, Any, Optional
#
#
# def foo(numbers: List[Any, str]) -> Optional[List[Tuple[int, int]]]:
#     return numbers

# расширенная типизация с python 3.9
# def bar(numbers: list[str, str]) -> list[tuple[int, int]] | None:
#     a: str = numbers[0]
#     return None
#
#
# bar(1234)

vklad = int(input())
procent = int(input())
# ставка рефинансирования б через сколько увеличится в два раза

# def calculate_deposit(vklad: float | int, procent: float | int, k: float | int) -> int:
#     years = 0
#     sum_za_2 = vklad*k
#     procent /= 100
#     while vklad <= sum_za_2:
#         vklad += vklad * procent
#         vklad = round(vklad, 2)
#         years += 1
#         print(f'{years=} {vklad=}')
#     return years
# print(calculate_deposit(
#     float(input('deposit: ')),
#     float(input('percent: ')),
#     float(input('k: ')))
# )

# C2H5OH -> {'C':2, 'H': 6, 'O': 1}
# C2H5OH -> {'C': 2, 'H': 6, 'O': 1}
# H2O -> {'H': 2, 'O': 1}

data = {}
formula = 'C2H5OH'
formula += '1' if formula[-1].isalpha() else ''
print(formula)

for i in range(len(formula)):
    if formula[i].isalpha():
        if formula[i+1].isdigit():
            if formula[i] in data:
                data[formula[i]] += int(formula[i+1])
            else:
                data[formula[i]] = int(formula[i+1])
        else:
            if formula[i] in data:
                data[formula[i]] += 1
            else:
                data[formula[i]] = 1
print(data)



