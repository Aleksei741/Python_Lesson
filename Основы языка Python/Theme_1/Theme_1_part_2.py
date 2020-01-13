
number = 0

while(True):
    number = int(input('Введите число: '))
    if (number > 0 and number < 10):
        print(number ** 2)
        break
    print('Число неверное.', end = ' ')
    print('Введите число больше 0, но меньше 10')