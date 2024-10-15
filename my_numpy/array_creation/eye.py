import numpy as np

# 创建一个 3x3 的单位矩阵
identity_matrix = np.eye(3)
print("3x3 的单位矩阵:\n", identity_matrix)
# 3x3 的单位矩阵:
#  [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# 创建一个非方阵,3x4 的矩阵，主对角线为 1，其余为 0
non_square_matrix = np.eye(3, 4)
print("3x4 的单位矩阵:\n", non_square_matrix)
# 3x4 的单位矩阵:
#  [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]]

# 创建具有不同对角线偏移的矩阵
# 主对角线
main_diag = np.eye(3, 3, k=0)
print("主对角线:\n", main_diag)
# 主对角线:
#  [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# 主对角线上方的第一条对角线
upper_diag = np.eye(3, 3, k=1)
print("主对角线上方的第一条对角线:\n", upper_diag)
# 主对角线上方的第一条对角线:
#  [[0. 1. 0.]
#  [0. 0. 1.]
#  [0. 0. 0.]]

# 主对角线下方的第一条对角线
lower_diag = np.eye(3, 3, k=-1)
print("主对角线下方的第一条对角线:\n", lower_diag)
# 主对角线下方的第一条对角线:
#  [[0. 0. 0.]
#  [1. 0. 0.]
#  [0. 1. 0.]]



# 创建一个整数类型的单位矩阵
int_identity = np.eye(3, dtype=int)
print("整数类型的单位矩阵:\n", int_identity)
# 整数类型的单位矩阵:
#  [[1 0 0]
#  [0 1 0]
#  [0 0 1]]

# 创建一个布尔类型的单位矩阵
bool_identity = np.eye(3, dtype=bool)
print("布尔类型的单位矩阵:\n", bool_identity)
# 布尔类型的单位矩阵:
#  [[ True False False]
#  [False  True False]
#  [False False  True]]

# 创建一个参考数组
reference = np.array([[1, 2], [3, 4]], dtype=np.float32)

# 使用 like 参数创建一个与 reference 兼容的单位矩阵
identity_like = np.eye(2, dtype=np.float32, like=reference)
print("与 reference 兼容的单位矩阵:\n", identity_like)
# 与 reference 兼容的单位矩阵:
#  [[1. 0.]
#  [0. 1.]]