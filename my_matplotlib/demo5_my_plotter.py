from matplotlib import pyplot as plt
import numpy as np


def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph.
    """
    out = ax.plot(data1, data2, **param_dict)
    return out


if __name__ == '__main__':
    # 生成一个4行每行长度为100的,服从标准正态分布（也称为高斯分布），即均值为 0，标准差为 1 的正态分布。
    data1, data2, data3, data4 = np.random.randn(4, 100)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
    my_plotter(ax1, data1, data2, {'marker': 'x'})
    my_plotter(ax2, data2, data3, {'marker': 'o'})
    ax1.set_title('Data1')
    ax2.set_title('Data2')
    fig.show()
