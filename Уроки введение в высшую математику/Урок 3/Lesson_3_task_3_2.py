import numpy as np
import matplotlib.pyplot as plt

R = 30
alfa = np.linspace(0, 2 * np.pi, 100)

print(alfa)

R_list = list()
for i in alfa:
    R_list.append(R)

#plt.plot(x, y)
plt.polar(alfa, R_list)
plt.title('Круг')  # заголовок
plt.xlabel('х')  # наименование оси абсцисс
plt.ylabel('у')  # наименование оси ординат

plt.show()
