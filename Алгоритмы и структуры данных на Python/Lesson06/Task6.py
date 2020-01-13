# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random
import sys, struct, ctypes


def show_size(x, level=0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}, id= {id(x)}')

    if isinstance(x, int):
        print('\t' * level, struct.unpack('LLl', ctypes.string_at(id(x), 12)))

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


print(sys.version)
# 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)]
print(sys.platform)
# win32

# n = int(input('Введите количество элементов масива: '))
# max_element = int(input('Введите значение mаксимально допустимого элемента массива: '))
# min_element = int(input('Введите значение mинимально допустимого элемента массива: '))
# mas = []
# for i in range(n):
#     mas.append(random.randint(min_element, max_element))

mas = [-1, 3, -4, 8, 5, 2, -3, -5, 8, -7]

print(f'Исходный массив:  {mas}')
print('Размерность массива: ')
show_size(mas)
# type= <class 'list'>, size= 76, object= [-1, 3, -4, 8, 5, 2, -3, -5, 8, -7], id= 8108792
#  type= <class 'int'>, size= 14, object= -1, id= 1876124736
#  (29, 1875957112, -1)
#  type= <class 'int'>, size= 14, object= 3, id= 1876124800
#  (33, 1875957112, 1)
#  type= <class 'int'>, size= 14, object= -4, id= 1876124688
#  (8, 1875957112, -1)
#  type= <class 'int'>, size= 14, object= 8, id= 1876124880
#  (47, 1875957112, 1)
#  type= <class 'int'>, size= 14, object= 5, id= 1876124832
#  (28, 1875957112, 1)
#  type= <class 'int'>, size= 14, object= 2, id= 1876124784
#  (79, 1875957112, 1)
#  type= <class 'int'>, size= 14, object= -3, id= 1876124704
#  (8, 1875957112, -1)
#  type= <class 'int'>, size= 14, object= -5, id= 1876124672
#  (7, 1875957112, -1)
#  type= <class 'int'>, size= 14, object= 8, id= 1876124880
#  (47, 1875957112, 1)
#  type= <class 'int'>, size= 14, object= -7, id= 1694944
#  (6, 1875957112, -1)

# ============================================================================
# Первый вариант
# ============================================================================
print('*' * 50)
print('Первый вариант:')
max_index_1 = 0
min_index_1 = 0

for i in range(len(mas)):
    if mas[i] > mas[max_index_1]:
        max_index_1 = i
    if mas[i] < mas[min_index_1]:
        min_index_1 = i

summ_1 = 0
if min_index_1 + 1 != max_index_1 and max_index_1 + 1 != min_index_1:
    if max_index_1 > min_index_1:
        for i in range(min_index_1 + 1, max_index_1):
            summ_1 += mas[i]
    else:
        for i in range(max_index_1 + 1, min_index_1):
            summ_1 += mas[i]

print(
    f'Максимальный элемент {mas[max_index_1]} по адресу {max_index_1}\nМинимальный элемент {mas[min_index_1]} по адресу {min_index_1}')
print(f'Cyммa элементов, находящихся между минимальным и максимальным элементами {summ_1}')
print('Максимальный и минимальные элементы:')
show_size(max_index_1)
show_size(min_index_1)
print('Результат:')
show_size(summ_1)
# Максимальный элемент 8 по адресу 3
# Минимальный элемент -7 по адресу 9
# Cyммa элементов, находящихся между минимальным и максимальным элементами 7
# Максимальный и минимальные элементы:
#  type= <class 'int'>, size= 14, object= 3, id= 1876124800
#  (33, 1875957112, 1)
#  type= <class 'int'>, size= 14, object= 9, id= 1876124896
#  (11, 1875957112, 1)
# Результат:
#  type= <class 'int'>, size= 14, object= 7, id= 1876124864
#  (18, 1875957112, 1)
# ============================================================================
# Второй вариант
# ============================================================================
print('*' * 50)
print('Второй вариант:')

max_index_2 = mas.index(max(mas))
min_index_2 = mas.index(min(mas))

summ_2 = 0
if min_index_2 + 1 != max_index_2 and max_index_2 + 1 != min_index_2:
    if max_index_2 > min_index_2:
        for i in range(min_index_2 + 1, max_index_2):
            summ_2 += mas[i]
    else:
        for i in range(max_index_2 + 1, min_index_2):
            summ_2 += mas[i]

print(
    f'Максимальный элемент {mas[max_index_2]} по адресу {max_index_2}\nМинимальный элемент {mas[min_index_2]} по адресу {min_index_2}')
print(f'Cyммa элементов, находящихся между минимальным и максимальным элементами {summ_2}')
print('Максимальный и минимальные элементы:')
show_size(max_index_2)
show_size(min_index_2)
print('Результат:')
show_size(summ_2)
# Максимальный элемент 8 по адресу 3
# Минимальный элемент -7 по адресу 9
# Cyммa элементов, находящихся между минимальным и максимальным элементами 7
# Максимальный и минимальные элементы:
#  type= <class 'int'>, size= 14, object= 3, id= 1876124800
#  (34, 1875957112, 1)
#  type= <class 'int'>, size= 14, object= 9, id= 1876124896
#  (12, 1875957112, 1)
# Результат:
#  type= <class 'int'>, size= 14, object= 7, id= 1876124864
#  (19, 1875957112, 1)

# ============================================================================
# Третий вариант
# ============================================================================
print('*' * 50)
print('Третий вариант:')

max_index_3 = mas.index(max(mas))
min_index_3 = mas.index(min(mas))

summ_3 = sum(mas[min_index_3 + 1:max_index_3] if min_index_3 <= max_index_3 else mas[max_index_3 + 1:min_index_3])

print(
    f'Максимальный элемент {mas[max_index_3]} по адресу {max_index_3}\nМинимальный элемент {mas[min_index_3]} по адресу {min_index_3}')
print(f'Cyммa элементов, находящихся между минимальным и максимальным элементами {summ_3}')
print('Максимальный и минимальные элементы:')
show_size(max_index_3)
show_size(min_index_3)
print('Результат:')
show_size(summ_3)
# Максимальный элемент 8 по адресу 3
# Минимальный элемент -7 по адресу 9
# Cyммa элементов, находящихся между минимальным и максимальным элементами 7
# Максимальный и минимальные элементы:
#  type= <class 'int'>, size= 14, object= 3, id= 1876124800
#  (35, 1875957112, 1)
#  type= <class 'int'>, size= 14, object= 9, id= 1876124896
#  (13, 1875957112, 1)
# Результат:
#  type= <class 'int'>, size= 14, object= 7, id= 1876124864
#  (20, 1875957112, 1)

# Вывод:
# От перемены алгоритма размеры хранимых данных не меняются. Растет лиш количество ссылок,
# что можно проследить по выводу функции struct.unpack('LLl', ctypes.string_at(id(x), 12))