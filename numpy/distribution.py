import numpy as np
import matplotlib.pyplot as plt


x = np.random.uniform(0.0, 50.0, 250)

print(x)

plt.hist(x, 5)
plt.show()

x = np.random.normal(5.0, 1.0, 10000)

plt.hist(x, 10)
plt.show()