n = 7

user_number = int(input('Угадай число: '))
while user_number != n:
    if user_number < n:
        print('Мое число больше, попробуйте снова')
    elif user_number > n:
        print('Мое число меньше, попробуйте снова')
    user_number = int(input('Угадай число: '))

print('Поздравляю! Вы угадали!')
