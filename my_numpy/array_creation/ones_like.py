import numpy as np

# 创建一个原型数组
prototype = np.array([[2, 3, 4], [5, 6, 7]])

# 使用 ones_like 创建全 1 数组
ones_array = np.ones_like(prototype)
print("与原型数组相同形状和类型的全 1 数组:\n", ones_array)
#  [[1 1 1]
#  [1 1 1]]

# 创建一个原型数组
prototype = np.array([0.5, 1.5, 2.5])

# 使用 ones_like 创建整数类型的全 1 数组
ones_int = np.ones_like(prototype, dtype=int)
print("整数类型的全 1 数组:", ones_int)
# 整数类型的全 1 数组: [1 1 1]
# 使用 ones_like 创建布尔类型的全 1 数组
ones_bool = np.ones_like(prototype, dtype=bool)
print("布尔类型的全 1 数组:", ones_bool)
# 布尔类型的全 1 数组: [ True  True  True]

# 创建一个原型数组
prototype = np.array([[1, 2], [3, 4]])

# 使用 ones_like 创建一个形状为 (3, 3) 的全 1 数组
ones_reshaped = np.ones_like(prototype, shape=(3, 3))
print("指定新形状的全 1 数组:\n", ones_reshaped)
# 指定新形状的全 1 数组:
#  [[1 1 1]
#  [1 1 1]
#  [1 1 1]]

# 定义一个自定义子类
class MyArray(np.ndarray):
    pass

# 创建一个原型数组的子类实例
prototype = np.array([1, 2, 3]).view(MyArray)

# 使用 ones_like 创建未初始化的子类数组
ones_subclass = np.ones_like(prototype, subok=True)
print("子类类型的全 1 数组类型:", type(ones_subclass))
# 子类类型的全 1 数组类型: <class '__main__.MyArray'>
print("子类类型的全 1 数组内容:", ones_subclass)
# 子类类型的全 1 数组内容: [1 1 1]

ones_subclass1 = np.ones_like(prototype, subok=False)
print("子类类型的全 1 数组类型:", type(ones_subclass1))
# 子类类型的全 1 数组类型: <class 'numpy.ndarray'>
print("子类类型的全 1 数组内容:", ones_subclass1)
# 子类类型的全 1 数组内容: [1 1 1]