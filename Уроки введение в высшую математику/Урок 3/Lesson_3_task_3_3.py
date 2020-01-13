import numpy as np
import matplotlib.pyplot as plt

n = 100

x = np.linspace(0, 10, n)

y = list()
for i in x:
    y.append(2*i+1)

R = list()
alfa = list()


for i in range(n):
    R.append(np.sqrt(x[i]**2 + y[i]**2))
    alfa.append(np.arcsin(y[i] / R[i]))

print(alfa)
print(R)

#plt.plot(x, y)
plt.polar(alfa, R)
plt.title('Круг')  # заголовок
plt.xlabel('х')  # наименование оси абсцисс
plt.ylabel('у')  # наименование оси ординат

plt.show()
