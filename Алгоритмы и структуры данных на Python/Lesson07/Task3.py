# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

import random

print('Массив размером 2m + 1')
m = int(input('Введите m: '))
n = 2 * m + 1
max_element = int(input('Введите значение mаксимально допустимого элемента массива: '))
min_element = int(input('Введите значение mинимально допустимого элемента массива: '))

mas = []
for i in range(n):
    mas.append(random.randint(min_element, max_element))

#mas = [0, 3, 1, 4, 1, 4, 5, 1, 1, 1, 0, 5, 1, 0, 1, 1, 5, 5, 4, 3, 0]
def mediana_(array):
    count = len(mas)
    for i in range(len(mas)):
        more = 0
        smal = 0
        ravn = 0
        for j in range(len(mas)):
            if (mas[i] < mas[j]):
                smal += 1
            elif (mas[i] > mas[j]):
                more += 1
            elif (mas[i] == mas[j]) and (i != j):
                ravn += 1

        # if ((smal == more) or (max(smal, more) - ravn) == min(smal, more)) and (smal+more+ravn == len(mas) - 1):
        #     result = mas[i]
        #     break

        if count > max(smal, more) - min(smal, more) - ravn:
            count = max(smal, more) - min(smal, more) - ravn
            result = mas[i]

    return result


mas2 = mas[:]
mas2.sort()
print(f'Сортированный массив: {mas2}')
print(f'Медианa вcтроеным методом: {mas2[m]}')

print(f'Исходный массив:      {mas}')
print(f'Медианa моим методом: {mediana_(mas)}')
