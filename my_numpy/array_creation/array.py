import numpy as np

# 从列表创建数组
arr = np.array([1, 2, 3, 4])
print(arr)
# [1 2 3 4]

arr = np.array([1, 2, 3, 4], dtype=float)
print(arr)
# [1. 2. 3. 4.]

arr = np.array([1, 2, 3, 4], ndmin=2)
print(arr)
# [[1 2 3 4]]

arr1 = np.array([1, 2, 3])
arr2 = np.array(arr1, copy=False)
arr2[0] = 10

print("arr1:", arr1)
# arr1: [10  2  3]
print("arr2:", arr2)
# arr2: [10  2  3]

arr1 = np.array([1, 2, 3])
arr2 = np.array(arr1, copy=True)
arr2[0] = 11
print("arr1:", arr1)
# arr1: [1 2 3]
print("arr2:", arr2)
# arr2: [11  2  3]


arr_c = np.array([[1, 2], [3, 4]], order='C')
arr_f = np.array([[1, 2], [3, 4]], order='F')

print("C-order:", arr_c)
print("F-order:", arr_f)


# [[1 2]
#  [3 4]]
# 尽管内容相同，内存布局不同。C-order 是行优先顺序，F-order 是列优先顺序。

class MyArray(np.ndarray):
    pass


arr1 = np.array([1, 2, 3]).view(MyArray)
arr2 = np.array(arr1, subok=True)
arr3 = np.array(arr1, subok=False)

print(type(arr1))
# <class '__main__.MyArray'>
print(type(arr2))
# <class '__main__.MyArray'>
print(type(arr3))
# <class 'numpy.ndarray'>

# 用 like 参数
reference = np.array([1, 2, 3])
arr = np.array([10, 20, 30], like=reference)
print(arr)
# [10 20 30]
