
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

def summa_v_god(vklad, procent):
    years = 0
    sum_za_2 = vklad*2
    procent /= 100
    while vklad <= sum_za_2:
        vklad += vklad * procent
        vklad = round(vklad,2)
        years += 1
        print(f'{years=} {vklad=}')
    return years
print(summa_v_god(vklad, procent))

