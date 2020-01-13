#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

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

sum = 0
if min_index + 1 != max_index and max_index + 1 != min_index:
    if max_index > min_index:
        for i in range(min_index + 1, max_index):
            sum += mas[i]
    else:
        for i in range(max_index + 1, min_index):
            sum += mas[i]

print(f'Исходный массив:  {mas}')
print(f'Максимальный элемент {mas[max_index]} по адресу {max_index}\nМинимальный элемент {mas[min_index]} по адресу {min_index}')
print(f'Cyммa элементов, находящихся между минимальным и максимальным элементами {sum}')