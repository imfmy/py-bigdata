import numpy as np

a = [1, 2]
print(np.asarray(a))
# array([1, 2])


a = np.array([1, 2])
print(np.asarray(a) is a)
# True
print(np.array(a) is a)
# False

arr = np.array([10, 20, 30])
arr_copy = np.asarray(arr, copy=False)

arr_copy[0] = 100
print(arr)  # arr 的第一个元素会被修改为 100
# [100  20  30]

arr = np.array([10, 20, 30])
arr_copy = np.asarray(arr, copy=True)

arr_copy[0] = 100
print(arr)  # arr 的第一个元素会被修改为 100
# [10 20 30]
