import math
import random

def list_sqrt(input_list = []):
    return [(i if i < 0 else math.sqrt(i)) for i in input_list] #Все требования в одной строчке :)

numbers_list = []
for i in range(20):
    numbers_list.append(random.randint(-100, 100))

print('Исходный список: ')
for i in numbers_list:
    print('{:>5.2f}'.format(i), end = '; ')
print()
print('Финальный список: ')
for i in list_sqrt(numbers_list):
    print('{:>5.2f}'.format(i), end = '; ')