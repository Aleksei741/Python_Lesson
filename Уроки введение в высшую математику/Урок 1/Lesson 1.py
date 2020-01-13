import math as math
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

#y(x)=cos(x)
y1 = []
for i in x:
    y1.append(math.cos(i))

#y(x)=cos(2x)
y2 = []
for i in x:
    y2.append(math.cos(2 * i))

plt.plot(x, y1, x, y2)
plt.legend(('cos(x)', 'cos(2x)'))  # подписи
plt.title('Trigonometry')  # заголовок
plt.xlabel('ед')  # наименование оси абсцисс
plt.ylabel('-')  # наименование оси ординат

plt.show()

