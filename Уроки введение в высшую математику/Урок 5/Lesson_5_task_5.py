import numpy as np
import matplotlib.pyplot as plt

n = 100
r = 0.7
x = np.random.rand(n)
y = r*x + (1-r)*np.random.rand(n)
plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

a = (np.sum(x)*np.sum(y) - n*np.sum(x*y))/(np.sum(x)*np.sum(x) - n*np.sum(x*x))
b = (np.sum(y) - a*np.sum(x))/n
Xm = np.sum(x) / n
Ym = np.sum(y) / n
x_y = list()
x_x = list()
y_y = list()
for i in range(len(x)):
    x_y.append((x[i] - Xm)*(y[i] - Ym))
    x_x.append((x[i] - Xm)**2)
    y_y.append((y[i] - Ym)**2)
R = (np.sum(x_y)) / (np.sqrt(np.sum(x_x)*np.sum(y_y)))

A = np.vstack([x, np.ones(len(x))]).T
a1, b1 = np.linalg.lstsq(A, y)[0]
print(a, b)
print(a1, b1)
print(f'Коэффициент корреляции: {R}')
plt.plot([0,1], [b, a+b])
plt.show()
