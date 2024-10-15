import numpy as np

# 创建一个二维数组
A = np.array([[1, 2, 3],
              [4, 5, 6]])
# 创建一个一维数组
B = np.array([10, 20, 30])

# 直接相加会发生广播
C = A + B
print("直接相加结果:\n", C)
# 直接相加结果:
#  [[11 22 33]
#  [14 25 36]]

# 使用 newaxis 调整维度后相加
B_col = B[np.newaxis, :]
print(B_col)
# [[10 20 30]]
C_new = A + B_col
print("使用 newaxis 后相加结果:\n", C_new)
# 使用 newaxis 后相加结果:
#  [[11 22 33]
#  [14 25 36]]


arr = np.array([1, 2, 3, 4])
# 使用 reshape
arr_reshaped = arr.reshape((4, 1))
print("使用 reshape 后的形状:", arr_reshaped.shape)
# 使用 reshape 后的形状: (4, 1)

# 使用 newaxis
arr_newaxis = arr[:, np.newaxis]
print("使用 newaxis 后的形状:", arr_newaxis.shape)
# 使用 newaxis 后的形状: (4, 1)

# 可以在同一个数组中多次使用 newaxis 来增加多个维度。
arr = np.array([1, 2, 3])
arr_expanded = arr[np.newaxis, :, np.newaxis]
print("增加多个维度后的形状:", arr_expanded.shape)
# 增加多个维度后的形状: (1, 3, 1)