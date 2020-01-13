import math as math
import numpy as np
import matplotlib.pyplot as plt



R = 30
x0 = 1
y0 = 25

x = np.linspace(x0+R, x0-R, 100)

y1 = []
y2 = []
for i in x:
    y1.append(math.sqrt(R**2 - (i - x0)**2) + y0)
    y2.append(-math.sqrt(R ** 2 - (i - x0) ** 2) + y0)

plt.plot(x, y1, x, y2)
plt.title('Круг')  # заголовок
plt.xlabel('х')  # наименование оси абсцисс
plt.ylabel('у')  # наименование оси ординат

plt.show()
