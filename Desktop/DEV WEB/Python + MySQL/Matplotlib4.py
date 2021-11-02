import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
axis = fig.gca(projection='3d')
theta = np.linspace(0,6*np.pi,100)
x = np.sin(theta)
y = np.cos(theta)
axis.plot(x,y, theta)
plt.show()


x = np.arange(-5,5,0.25)
y = np.arange(-5,5,0.25)
x, y = np.meshgrid(x,y)
z = (x**2 + y**2)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x,y,z)

plt.show()