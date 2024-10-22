import numpy as np

# 从列表转换为数组
arr = np.asanyarray([1, 2, 3, 4])
print(arr)
# [1 2 3 4]

mat = np.matrix([[1, 2], [3, 4]])
arr = np.asanyarray(mat)
print(type(arr))  # 仍然是 np.matrix 类型
# <class 'numpy.matrix'>

arr = np.array([[1, 2], [3, 4]])
sub_arr = np.asanyarray(arr)
print(type(sub_arr))  # 仍然是 np.ndarray 类型
# <class 'numpy.ndarray'>
