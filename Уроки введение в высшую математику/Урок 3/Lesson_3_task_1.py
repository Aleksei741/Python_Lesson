import math as math
import numpy as np
import matplotlib.pyplot as plt
import random

x = np.linspace(0, 10, 100)


#y(x) = k∙cos(x – a) + b
y = []
for i in range(3):
    y.append(list())
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    k = random.randint(0, 10)
    for j in x:
        y[i].append(k * math.cos(j - a) + b)

plt.plot(x, y[0], x, y[1], x, y[2])
plt.xlabel('x')  # наименование оси абсцисс
plt.ylabel('y')  # наименование оси ординат

plt.show()
