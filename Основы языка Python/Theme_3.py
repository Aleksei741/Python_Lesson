import keyboard  # using module keyboard
import random as rnd

print('Загадайте число от 1 до 100\n')

print('На экране будет выводится число')
print('Нажимайте стрелку влево если загаданое число меньше ')
print('Нажимайте стрелку вправо если загаданое число больше')
print('Нажмите = если число отгадано')
print('Нажмите esc если хотите выйти из игры')

print('\nНажмите любую клавишу')
keyboard.read_hotkey(suppress = False)

key = ''
min_number = 1
max_number = 100
number = rnd.randint(40, 60)
iterations = 0

while key != '=':

    print(' ')
    print('Это число {}'.format(number))
    for i in range(1, 101):
        if i == min_number:
            print('{}'.format(min_number), end='')
        elif i == max_number:
            print('{}'.format(max_number), end='')
        #elif i < min_number or i > max_number:
            #print('-', end='')
        elif i == number:
            print(' {} '.format(number), end='')
        elif min_number < i < max_number:
            print('*', end='')
    print(' ')

    key = keyboard.read_hotkey(suppress = False)
    if key == 'left':
        max_number = number - 1
    elif key == 'right':
        min_number = number + 1
    elif key == 'esc':
        break

    if min_number == max_number:
        print('Это число {} \nКомпьютер выйграл за {} шагов'.format(max_number, iterations))
        break
    elif min_number > max_number:
        print('Так не бывает')
        break

    if key == 'left' or key == 'right':
        number = rnd.randint(min_number, max_number)
        iterations += 1
else:
    print('Компьютер выйграл за {} шагов'.format(iterations))

print('\nНажмите любую клавишу')
keyboard.read_hotkey(suppress = False)