# pyplot-style
import matplotlib.pyplot as plt
import numpy as np

# 生成样例数据
x = np.linspace(0, 2, 100)
plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(x, x, label='linear')
plt.plot(x, x ** 2, label='quadratic')
plt.plot(x, x **3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Plot Title')
plt.legend()
plt.show()
