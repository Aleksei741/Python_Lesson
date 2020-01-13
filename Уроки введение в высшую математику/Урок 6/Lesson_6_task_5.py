import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.linalg
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

# 5. Найдите нормальное псевдорешение недоопределенной системы:
# x + 2y – z = 1
# 8x – 5y + 2z = 12
# Для этого определите функцию Q(x,y,z), равную норме решения, и найдите ее минимум.

def Q(x, y, z):
    return np.sqrt(x**2 + y**2 + z**2)

fig2 = figure()
ax = Axes3D(fig2)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)

ax.plot_surface(X, Y, Q(X, Y, X + 2*Y - 1))
ax.plot_surface(X, Y, Q(X, Y, 12 - 8*X+5*Y))
ax.scatter(0,0,0,'z',50,'red')
show()

A = np.array([[1, 2, -1], [8, -5, 2]])
B = np.array([1, 12])

print(f'Ответ: {np.linalg.lstsq(A,B, rcond=-1)}')
#Ответ: (array([ 1.38191882, -0.18081181,  0.0202952 ]), array([], dtype=float64), 2, array([9.65316119, 2.41173777]))