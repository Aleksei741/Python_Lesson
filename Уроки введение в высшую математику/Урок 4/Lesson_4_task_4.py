import math as math
import numpy as np
import matplotlib.pyplot as plt



x = np.linspace(100, 500, 1000)
a = np.linspace(0.01, 0.02, 100)

x_1 = list()
a_1 = list()
for i in range(len(a)):
    t = math.pi / a[i]
    if t < 500 and t > 100:
        x_1.append(t)
        a_1.append(a[i])

x_2 = list()
a_2 = list()
for i in range(len(a)):
    t = math.pi * 2 / a[i]
    if t < 500 and t > 100:
        x_2.append(t)
        a_2.append(a[i])

x_3 = list()
a_3 = list()
for i in range(len(a)):
    t = math.pi * 3 / a[i]
    if t < 500 and t > 100:
        x_3.append(t)
        a_3.append(a[i])

#plt.plot( x1,y1 )
plt.plot(a_1, x_1, a_2, x_2, a_3, x_3)
plt.xlabel('a')  # наименование оси абсцисс
plt.ylabel('x')  # наименование оси ординат

plt.show()


