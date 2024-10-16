import numpy as np

# 创建一个 4x4 的单位矩阵
identity_matrix = np.identity(4)
print(identity_matrix)
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

# 创建一个整数类型的 3x3 单位矩阵
int_identity = np.identity(3, dtype=int)
print("整数类型的 3x3 单位矩阵:\n", int_identity)
# 整数类型的 3x3 单位矩阵:
#  [[1 0 0]
#  [0 1 0]
#  [0 0 1]]

# 创建一个布尔类型的 2x2 单位矩阵
bool_identity = np.identity(2, dtype=bool)
print("布尔类型的 2x2 单位矩阵:\n", bool_identity)
# 布尔类型的 2x2 单位矩阵:
#  [[ True False]
#  [False  True]]

# 创建一个参考数组
reference = np.array([[10, 20], [30, 40]], dtype=np.float32)

# 使用 like 参数创建一个与 reference 兼容的单位矩阵
identity_like = np.identity(2, dtype=np.float32, like=reference)
print("与 reference 兼容的单位矩阵:\n", identity_like)
# 与 reference 兼容的单位矩阵:
#  [[1. 0.]
#  [0. 1.]]