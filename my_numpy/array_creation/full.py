import numpy as np

# 创建一个长度为 5 的一维数组，所有元素为 7
full_array = np.full(5, 7)
print("一维全 7 数组:\n", full_array)
# 一维全 7 数组:
#  [7 7 7 7 7]

# 创建一个 3x4 的二维数组，所有元素为 3.14
pi_matrix = np.full((3, 4), 3.14)
print("3x4 的二维全 3.14 矩阵:\n", pi_matrix)
# 3x4 的二维全 3.14 矩阵:
#  [[3.14 3.14 3.14 3.14]
#  [3.14 3.14 3.14 3.14]
#  [3.14 3.14 3.14 3.14]]

# 创建一个布尔类型的 2x2 数组，所有元素为 True
bool_full = np.full((2, 2), True, dtype=bool)
print("布尔类型的 2x2 全 True 数组:\n", bool_full)
# 布尔类型的 2x2 全 True 数组:
#  [[ True  True]
#  [ True  True]]
