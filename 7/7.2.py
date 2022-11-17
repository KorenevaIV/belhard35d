# 2. «Ведьмаку заплатите чеканной монетой»
# Имеются монеты номиналом 1/5/10/25 копеек, написать функцию witcher, принимающая
# сумму в копейках, необходимо рассчитать сколько минимальное количество монет
# номиналом 1/5/10/25 необходимо чтобы составить данную сумму. Прим. 66 = 25 + 25 + 10 + 5
# + 1 ответ 5 монет
def witcher(total_sum: int)-> int:
    coins=0
    coins+=total_sum//25
    total_sum%=25
    coins+=total_sum//10
    total_sum%=10
    coins+=total_sum//5
    total_sum%=5
    coins+=total_sum
    return coins
print(witcher(66))
