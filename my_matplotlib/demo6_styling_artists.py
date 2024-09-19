from matplotlib import pyplot as plt
import numpy as np

data1, data2, data3, data4 = np.random.randn(4, 100)
x = np.arange(len(data1))
y = np.cumsum(data1)
fig, ax = plt.subplots(figsize=(5, 2.7))
ax.plot(x, y, color='blue', linewidth=3, linestyle='--', label='data1')
l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2)
l.set_linestyle(':')
l.set_label('data2')
ax.plot(x, np.cumsum(data3))
ax.legend()
fig.show()
