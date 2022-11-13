#Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int
def binnum(n):
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s
while 1:
    n = int(input())
    if n != 0:
        print(binnum(n))
    else:
        break

s = binnum(n)
def bin_to_dec(s):
    dlina = len(s)
    print(dlina)
    chislo_dec = 0
    for i in range(0, dlina):
        chislo_dec = chislo_dec + int(s[i]) * (2 ** (dlina - i - 1))
    return chislo_dec
print(chislo_dec)
