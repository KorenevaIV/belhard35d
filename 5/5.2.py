# сделать калькулятор: пользователь вводит число затеи действие и второе число
first_num = int(input('Enter first number: '))
text = input('what to do? ')
second_num = int(input('Enter second number: '))

if text == '*':
    print(first_num*second_num)
elif text == '/':
    if second_num == 0:
        print('Please enter other number, not zero')
elif text == '/':
    print(first_num/second_num)
elif text == '+':
    print(first_num+second_num)
elif text == '-':
    print(first_num-second_num)
elif text == '**':
    print(first_num**second_num)
else:
    print(f'crazy choice, please try again')




