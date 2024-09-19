import matplotlib.pyplot as plt
import numpy as np

# use the OO-style
# 返回一个在指定间隔[0,2]内100个均匀分布分布数字
x = np.linspace(0, 2, 100)
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')

ax.set_title("Simple Plot")
ax.plot(x, x, label='linear')
ax.plot(x, x ** 2, label='quadratic')
ax.plot(x, x ** 3, label='cubic')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
# 为以上曲线添加图例说明
ax.legend()
fig.show()
