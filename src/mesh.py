import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = plt.axes(projection='3d')
def z_func(x,y):
    return np.sin(np.sqrt(x**2+y**2))
y = np.linspace(-5,5,100)
x = np.linspace(-5,5,100)
X,Y = np.meshgrid(x,y)
Z = z_func(X,Y)
ax.plot_surface(X,Y,Z)

plt.show()
