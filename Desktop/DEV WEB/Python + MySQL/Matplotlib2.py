import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10,0.1)
y = x ** 2
h = x ** 3
fig = plt.figure()
axis = fig.add_axes([0.3,0.3,1,1])
axis.set_title("Parábola")
axis.plot(x,y,label="Crescimento Quadrático")
axis.plot(x,h, label="Crescimento Cúbico")
plt.legend()
plt.show()