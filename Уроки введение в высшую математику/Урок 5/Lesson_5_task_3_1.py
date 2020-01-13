import numpy as np
import math

k = 0
n = 10

a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)

x = a + b + c + d

for i in range(n):
    if x[i] == 2:
        k = k + 1

print(f'Количество успехов: {k} \nКоличество испытаний: {n}\nОценка вероятности: {k/n}')



#Задание непонятно
print('Расчетные значения:')
k = 2
print(f'Вероятность того, что за {n} испытаний выпадет две еденицы {k} раз считается так:')
C = math.factorial(n)/(math.factorial(k)*math.factorial(n - k))
P = C *(1/2)**k * (1/2)**(n-k)
print(f'Коэфициент, при k = {k} успехов n = {n} испытаний, равен: {C}')
print(f'Вероятность P(k) = {P}, считается по формуле P = C *(1/2)**k * (1/2)**(n-k)')
print('Что и является ответом на эту задачу')

k = 2
print(f'Вероятность того, что за {n} испытаний выпадет две еденицы {k} раз считается так:')
C = math.factorial(n)/(math.factorial(k)*math.factorial(n - k))
P = C *(1/5)**k * (4/5)**(n-k)
print(f'Коэфициент, при k = {k} успехов n = {n} испытаний, равен: {C}')
print(f'Вероятность P(k) = {P}, считается по формуле P = C *(1/5)**k * (4/5)**(n-k)')
print('Всего 5 вариантов: 0 - 1ца не выпадала\n 1 - 1ца выпала 1ин раз\n 2 - 1ца выпала 2ва раза\n итд до 4 (5ть вариантов)')


