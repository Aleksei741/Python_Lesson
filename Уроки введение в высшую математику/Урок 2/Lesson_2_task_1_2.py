from math import sqrt

print('Введите координаты вектора')

x = int(input(f'Введите координату x: '))
y = int(input(f'Введите координату y: '))
z = int(input(f'Введите координату z: '))

print(f'Длина вектора {sqrt(x**2 + y**2 + z*z)}')