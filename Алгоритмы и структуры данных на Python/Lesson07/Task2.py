# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

def pour(l_list, r_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    for _ in range(len(l_list) + len(r_list)):

        if left_list_index < len(l_list) and right_list_index < len(r_list):

            if l_list[left_list_index] <= r_list[right_list_index]:
                sorted_list.append(l_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(r_list[right_list_index])
                right_list_index += 1
        elif left_list_index == len(l_list):
            sorted_list.append(r_list[right_list_index])
            right_list_index += 1
        elif right_list_index == len(r_list):
            sorted_list.append(l_list[left_list_index])
            left_list_index += 1

    return sorted_list


def sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    l_list = sort(array[:mid])
    r_list = sort(array[mid:])

    return pour(l_list, r_list)


import random

n = int(input('Введите количество элементов масива: '))
min_element = 0  # int(input('Введите значение mаксимально допустимого элемента массива: '))
max_element = 50  # int(input('Введите значение mинимально допустимого элемента массива: '))

mas = []
for i in range(n):
    mas.append(random.randint(min_element, max_element))

result = sort(mas)
print(f'Исходный массив: {mas}')
print(f'Результат      : {result}')
