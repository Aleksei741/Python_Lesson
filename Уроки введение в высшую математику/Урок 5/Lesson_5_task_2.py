import numpy as np

f = list()
f1 = list()
for i in range(37):
    f.append(0)
    f1.append(0)

n = 100000
number1 = 3
number2 = 5
count = 0
for i in range(n):
    x = np.random.randint(0, 37)
    x1 = np.random.randint(0, 37)
    f[x] = f[x] + 1
    if x == number1 and x1 == number2:
        count = count + 1

for i in range(len(f)):
    print(f'Значение {i} выпало f {f[i]} раз ')

print(f'Число {number1} выпадает с вероятностью {f[number1] / n}')
print(f'Расчетная вероятность выпадения числа {number1} будет {1/37}')
#Сложение
print(f'Число {number1} или {number2} выпадает с вероятностью {f[number1] / n + f[number1] / n}')
print(f'Расчетная вероятность выпадения чисел {number1} или {number2} будет {1/37 + 1/37}')
#Умножение
print(f'Число {number1} и {number2} в двух выборках выпадает с вероятностью {count / n}')
print(f'Расчетная вероятность выпадения чисел {number1} и {number2} в двух выборках будет {1/37 * 1/37}')
