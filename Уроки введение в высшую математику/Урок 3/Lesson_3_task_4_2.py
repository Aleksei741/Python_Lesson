import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt


def equations(p):
    x,y = p
    return y - x**2 + 1, np.exp(x) + x * (1 - y) - 1

x1 , y1 = fsolve(equations , (-2,3))
x2 , y2 = fsolve(equations , (3,10))
x3 , y3 = fsolve(equations , (4,15))

print(x1, y1)
print(x2, y2)
print(x3, y3)

mas_x = [x1, x2, x3]
mas_x.sort()

test_point = list()

k = (min(mas_x) + max(mas_x))/2
test_point.append(mas_x[0] - k)
for j in range(len(mas_x) - 1):
    test_point.append((mas_x[j] + mas_x[j+1]) / 2)
test_point.append(mas_x[len(mas_x) - 1] + k)



print(mas_x)
print(test_point)

answer = list()
for i in range(len(test_point)):
    y = test_point[i] ** 2 - 1
    a = (np.exp(test_point[i]) + test_point[i] -1)/test_point[i]
    if a > y:
        if i == 0:
            answer.append([float('-inf'), mas_x[i]])
        elif i < len(mas_x):
            answer.append([mas_x[i-1], mas_x[i]])
        else:
            answer.append([mas_x[i - 1], float('inf')])

print(f'Ответ: {answer}')