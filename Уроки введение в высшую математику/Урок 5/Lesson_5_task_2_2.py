import numpy as np

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

n = 10
x = list()
result = list()
num_bins = 5

for i in range(10):
    y = np.random.rand(10)
    x.append(y)

print('Матрица х построчно:')
for i in x:
    print(i)
    result.append(i.sum())

print('Вектор result:')
print(result)

n, bins, patches = plt.hist(result, num_bins)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Histogram')
plt.show()