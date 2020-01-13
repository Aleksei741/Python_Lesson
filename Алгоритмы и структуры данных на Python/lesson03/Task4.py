#4. Определить, какое число в массиве встречается чаще всего.

import random

n = int(input('Введите количество элементов масива: '))
min_element = int(input('Введите значение mаксимально допустимого элемента массива: '))
max_element = int(input('Введите значение mинимально допустимого элемента массива: '))
mas = []
for i in range(n):
    mas.append(random.randint(min_element, max_element))

data_set = set(mas)
max_elem = 0
max_count = 0

for i in data_set:
    #count = mas.count(i)
    count = 0
    for j in mas:
        if j == i:
            count += 1
    if(count > max_count):
        max_count = count
        max_elem = i

print(f'Исходный массив:  {mas}')
if max_count > 1:
    print(f'Eлемент {max_elem} встречается {max_count} раз')
else:
    print('Все элементы разные')
