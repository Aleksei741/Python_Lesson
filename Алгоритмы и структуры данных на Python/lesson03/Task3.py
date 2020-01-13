# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

n = int(input('Введите количество элементов масива: '))
min_element = int(input('Введите значение mаксимально допустимого элемента массива: '))
max_element = int(input('Введите значение mинимально допустимого элемента массива: '))

mas = []
for i in range(n):
    mas.append(random.randint(min_element, max_element))

max_index = 0
min_index = 0

for i in range(n):
    if mas[i] > mas[max_index]:
        max_index = i
    if mas[i] < mas[min_index]:
        min_index = i

print(f'Исходный массив:  {mas}')
bufer = mas[max_index]
mas[max_index] = mas[min_index]
mas[min_index] = bufer
print(f'Финальный массив: {mas}')
print(f'Индексы max: {max_index}, min: {min_index}')
