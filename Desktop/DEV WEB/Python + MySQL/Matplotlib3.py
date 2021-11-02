import numpy as np
import matplotlib.pyplot as plt

x = [np.random.normal(0, i+4, 100) for i in range(1,3)]
plt.boxplot(x)
plt.show()