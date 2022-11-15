#Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int.  def func(n):# ввод числа  двоичного
#                             print(int(n, base=2)) # приводимм к числу, с основанием(в 2-ичной системе и выоводим)
def binnum(n):
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s

n = int(input())
if n != 0:
    print(binnum(n))

def binary_to_decimal(binary):
    decimal = 0
    for i in binary[::-1]:
        decimal += int(i)
        decimal *= 2
    return decimal

def binary_to_dec2(binary):
    decimal = 0
    binary = binary[::-1]
    for i range(len(binary)):
        if binary[i] == '1':
            drcimal += 2 ** i
    return decimal


print(binary_to_decimal2(decimal_to_binary(decimal=18)))
#
# def bin_to_dec(n):
#     dlina = len(n)
#     chislo_dec = 0
#     for i in range(0, dlina):
#         chislo_dec = chislo_dec + int(n[i]) * (2 ** (dlina - i - 1))
#     return chislo_dec
# print(bin_to_dec(binnum(n)))







