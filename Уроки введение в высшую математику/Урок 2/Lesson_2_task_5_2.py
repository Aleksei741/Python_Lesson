from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import math

fig = figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.5)
Y = np. arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)
Z=X**2 + 5*Y**2
ax.plot_surface(X, Y, Z)
ax.scatter(0,0,0,'z',50,'red')
#show()

fig2 = figure()
ax2 = Axes3D(fig2)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)
Z=X**2 - Y**2 + 11
ax2.plot_wireframe(X, Y, Z)
ax2.scatter(0,0,0,'z',50,'red')
show()