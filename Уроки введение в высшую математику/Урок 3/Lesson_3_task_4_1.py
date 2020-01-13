import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve




def equations(p):
    x,y = p
    return y - x**2 + 1, np.exp(x) + x * (1 - y) - 1

x1 , y1 = fsolve(equations , (-2,3))
x2 , y2 = fsolve(equations , (3,10))
x3 , y3 = fsolve(equations , (4,15))

print(x1, y1)
print(x2, y2)
print(x3, y3)



x = np.linspace(-2, 4.5, 100)

y1 = []
y2 = []
for i in x:
    y1.append(i**2 - 1)
    y2.append((np.exp(i) + i -1)/i)

plt.plot(x, y1, x, y2)
plt.xlabel('х')  # наименование оси абсцисс
plt.ylabel('у')  # наименование оси ординат

plt.show()