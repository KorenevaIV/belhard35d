# сделать калькулятор: пользователь вводит число затеи действие и второе число
first_num = int(input('Enter number: '))
text = input('what to do? ')
second_num = int(input('Enter number: '))
if text == '*':
    print(first_num*second_num)
elif text == '/':
    print(first_num/second_num)
elif text == '+':
    print(first_num+second_num)
elif text == '-':
    print(first_num-second_num)
elif text == '**':
    print(first_num**second_num)
else:
    print('crazy choice')