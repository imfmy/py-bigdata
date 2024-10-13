import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])
print(np.e)
# 2.718281828459045

print(np.euler_gamma)
# 0.577215664901532


print(np.inf)
# inf
print(np.array([1]) / 0.)
# <input>:1: RuntimeWarning: divide by zero encountered in divide
# [inf]

print(type(np.nan))
# <class 'float'>
arr = np.array([1.0, 2.0, np.nan, 4.0, 5.0])
print("数组内容:", arr)
# 数组内容: [ 1.  2. nan  4.  5.]
nan_mask = np.isnan(arr)
print("是否为 nan:", nan_mask)
# 是否为 nan: [False False  True False False]

print(np.nan == np.nan)
# False
print(np.nan != np.nan)
# True
print(np.nan + 1)
# nan
print(np.log(-1))
# nan
print(np.log([-1, 1, 2]))
# [       nan 0.         0.69314718]

# 替换nan
arr = np.array([1.0, 2.0, np.nan, 4.0, 5.0])
# 用0替换 nan
arr_clean = np.where(np.isnan(arr), 0, arr)
print(arr_clean)
# [1. 2. 0. 4. 5.]

# 忽略nan
arr = np.array([1.0, 2.0, np.nan, 4.0, 5.0])
sum_val = np.nansum(arr)
sum_val2 = np.sum(arr)
print(sum_val)
# 12.0
print(sum_val2)
# nan

# numpy.newaxis
print(np.newaxis is None)
# True

# 增加一维
arr = np.array([1, 2, 3, 4])
print("原始数组形状:", arr.shape,arr)
# 原始数组形状: (4,)

# 使用 newaxis 增加一个新的维度
arr_col = arr[:, np.newaxis]
print("增加列维度后的形状:", arr_col.shape,arr_col)
# 增加列维度后的形状: (4, 1) [[1]
#  [2]
#  [3]
#  [4]]

arr_row = arr[np.newaxis, :]
print("增加行维度后的形状:", arr_row.shape,arr_row)
# 增加行维度后的形状: (1, 4) [[1 2 3 4]]

print(np.pi)
# 3.141592653589793
