# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

def selection_sort(array):
    iteration = 0
    for i in range(len(array)):
        iteration = i+1
        idx_min = i

        for j in range(i+1, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j

        array[idx_min], array[i] = array[i], array[idx_min]
        print(array)
    print(f'Количество итераций {iteration}')

def selection_sort_с(array):
    iteration = 0
    for i in range(len(array)):
        iteration += 1
        idx_min = i
        count = 0
        for j in range(i+1, len(array)):
            if array[j] < array[idx_min]:
                count += 1
                idx_min = j

        array[idx_min], array[i] = array[i], array[idx_min]

        if count == 0: #если массим типа отсортирован и проходов не требуется
            er = 0
            for j in range(i+1, len(array)): #Убеждаемся в этом, без этого сортировка не работает проверте на большем примере
                if array[j - 1] > array[j]:
                    er = 1
                    break
            if er == 0:
                break
        print(array)
    print(f'Количество итераций {iteration}')

import random

n = int(input('Введите количество элементов масива: '))
min_element = -100 # int(input('Введите значение mаксимально допустимого элемента массива: '))
max_element = 100 # int(input('Введите значение mинимально допустимого элемента массива: '))

mas = []
for i in range(n):
    mas.append(random.randint(min_element, max_element))
mas1 = mas[:]
mas2 = mas[:]


print('Сортировка без доработки')
selection_sort(mas1)
print('Сортировка с доработкой')
selection_sort_с(mas2)

print('Исходный массив')
print(mas)
print('Результат')
print(f'mas1 {mas1}')
print(f'mas2 {mas2}')