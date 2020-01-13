import math as m
import itertools

#Сочетание
n = 6
k = 3
print(f'Кол-во сочетаний: С = {m.factorial(n)/(m.factorial(k) * m.factorial(n - k))}')
for p in itertools.combinations('012345', k):
    print(''.join(str(x) for x in p))

#Размещение (два объекта из 4х возможных)
print('Размещение')
n = 5
k = 2
for p in itertools.permutations('01234', k):
    print(''.join(str(x) for x in p))