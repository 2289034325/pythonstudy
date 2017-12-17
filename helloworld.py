import numpy as np
import matplotlib.pyplot as plt

# print(np.sin(30 * np.pi / 180))

x = np.linspace(-10, 10, 1000)
#y = [1 / (1 + np.exp(-i)) for i in x]
y = [(1 / (1 + np.exp(-i)))*(1-(1 / (1 + np.exp(-i)))) for i in x]
plt.plot(x, y)

plt.show()
