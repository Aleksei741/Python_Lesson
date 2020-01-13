import random

numbers_list = []
for i in range(20):
    numbers_list.append(random.randint(-100, 100))

print('Исходный список: {}'.format(numbers_list))
print('Список элементов, кратных 3: {}'.format([number for number in numbers_list if number % 3 == 0]))
print('Список положительных элементов: {}'.format([number for number in numbers_list if number > 0]))
print('Список элементов, не кратных 4: {}'.format([number for number in numbers_list if number % 4 != 0]))