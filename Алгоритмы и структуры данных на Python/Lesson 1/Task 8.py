#8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if b < a < c or c < a < b:
    print(f'Среднее: {a}')
elif c < b < a or a < b < c:
    print(f'Среднее: {b}')
elif a < c < b or b < c < a:
    print(f'Среднее: {c}')
else:
    print('Некорректные данные')
