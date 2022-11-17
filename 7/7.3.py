# 3. Написать функцию pow, которая принимает число А и число Б, необходимо с помощью
# рекурсии возвести число А в степень Б
def pow(number: int, power: int) -> int:
    if power == 1:
        return number
    if power != 1:
        return number * pow(number, power - 1)


number = int(input("Enter number: "))
power = int(input("Enter power: "))
print('Result: ', pow(number, power))
