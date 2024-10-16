import numpy as np

# 创建一个长度为 5 的一维数组，元素类型为 float
ones_array = np.ones(5)
print("一维全 1 数组:\n", ones_array)
#  [1. 1. 1. 1. 1.]

# 创建一个 3x4 的二维数组，元素类型为 float
ones_matrix = np.ones((3, 4))
print("3x4 的二维全 1 矩阵:\n", ones_matrix)
#  [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

# 创建一个布尔类型的 2x2 数组
ones_bool = np.ones((2, 2), dtype=bool)
print("布尔类型的 2x2 全 1 数组:\n", ones_bool)
# 布尔类型的 2x2 全 1 数组:
#  [[ True  True]
#  [ True  True]]

# 创建一个按列优先顺序的 2x2 数组
ones_f_order = np.ones((2, 2), order='F')
print("Fortran-style 的 2x2 全 1 数组:\n", ones_f_order)
# Fortran-style 的 2x2 全 1 数组:
#  [[1. 1.]
#  [1. 1.]]
# 虽然输出看起来相同，但内存中的存储顺序不同。order 参数主要影响底层内存布局，对用于指定数组存储的设备（如 GPU）。在标准的 NumPy 使用中，通常不需要设置此参数，主要在与支持多设备计算的库集成时使用。于某些需要特定内存布局的高性能计算有影响。

# 创建一个参考数组
reference = np.array([[10, 20], [30, 40]], dtype=np.float32)

# 使用 like 参数创建一个与 reference 兼容的全 1 数组
ones_like = np.ones((2, 2), dtype=np.float32, like=reference)
print("与 reference 兼容的全 1 数组:\n", ones_like)
# 与 reference 兼容的全 1 数组:
#  [[1. 1.]
#  [1. 1.]]
