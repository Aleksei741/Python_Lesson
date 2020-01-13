import random as rnd


def game():
    print('Загадайте число от 1 до 100\n')
    print('На экране будет выводится число')
    print('Введите "<" если загаданное число меньше')
    print('Введите ">" если загаданое число больше')
    print('Введите "=" если число отгадано')
    print('Введите "exit" если хотите выйти из игры')

    input('Нажмите Enter')

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
            # elif i < min_number or i > max_number:
            # print('-', end='')
            elif i == number:
                print(' {} '.format(number), end='')
            elif min_number < i < max_number:
                print('*', end='')
        print(' ')

        key = input('Ваш ответ: ')
        if key == '<':
            max_number = number - 1
        elif key == '>':
            min_number = number + 1
        elif key == 'exit':
            break

        if min_number == max_number:
            print('Это число {} \nКомпьютер выйграл за {} шагов'.format(max_number, iterations))
            break
        elif min_number > max_number:
            print('Так не бывает')
            break

        if key == '<' or key == '>':
            number = rnd.randint(min_number, max_number)
            iterations += 1
    else:
        print('Компьютер выйграл за {} шагов'.format(iterations))


if __name__ == '__main__':
    game()
