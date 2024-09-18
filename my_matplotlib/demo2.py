import matplotlib.pyplot as plt
import numpy as np
# 初始化随机数生成器的状态，从而使得随机数的生成过程可重复。
np.random.seed(19680801)  # seed the random number generator.
# 如果再次运行这段代码，生成的随机数将会是相同的
random_numbers = np.random.rand(5)
# [0.7003673  0.74275081 0.70928001 0.56674552 0.97778533]
print(random_numbers)

# 生成一个[0,50)的递增数组：[0,2,3,..49]
a = np.arange(50)
# 生成一个长度为50的数组，每个元素为[0,50)的随机值[ 3,49,36 ..,25]
c = np.random.randint(0, 50, 50)
print(c)
# # 生成一个标准正态分布的随机数数组,数组长度为50
d = np.random.randn(50)
data = {'a': a,
        'c': c,
        'd': d}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(5, 1), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')
ax.set_title('scatter plot')
plt.show()
