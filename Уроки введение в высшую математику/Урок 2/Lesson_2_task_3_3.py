import math as math
import numpy as np
import matplotlib.pyplot as plt


a = -1
b = 1

x = np.linspace(-5*a-a, a, 100) + np.linspace(a, 5*a-a, 100)

y1 = []
y2 = []
for i in x:
    #print(f'{i} __ {b**2 + b**2 * i**2 / a**2}')
    y1.append(math.sqrt(b**2 + b**2 * i**2 / a**2))
    y2.append(-math.sqrt(b**2 + b**2 * i**2 / a**2))


plt.plot(x, y1, x, y2)
plt.title('Гипербола')  # заголовок
plt.xlabel('х')  # наименование оси абсцисс
plt.ylabel('у')  # наименование оси ординат

plt.show()
